from __future__ import annotations

import dataclasses
import enum
from functools import cached_property
from typing import Any, Iterator

import markdown_it.token
from markdown_it import MarkdownIt

from sdk.ipython_executor import IPythonCommand, IPythonExecutor
from sdk.python_exec_utils import eval_or_exec


class Language(enum.Enum):
    PYTHON = 'python'
    PYTHON_INTERACTIVE = 'python-interactive'
    IPYTHON = 'ipython'
    TXT = 'txt'
    BASH = 'bash'
    SQL = 'sql'


@dataclasses.dataclass
class ParagraphCode:
    body: str
    language: Language

    # {hide}
    # Hide this code from actual users,
    # (usually used for initialization or checking)
    hide: bool = False

    # {continue}
    # Run this code in context of previous code black,
    # meaning you can use variables defined in previous code block
    continue_code: bool = False

    # {merge}
    # Visually merge this block and the previous one
    # Cannot be used without {continue} since it doesn't make sense.
    merge: bool = False

    # {no-run}
    # Don't run this block at all
    no_run: bool = False

    # {python-interactive-no-check}
    # Every interactive python line is executed and result is checked against
    # the output line.
    # This flag disables this check.
    # This is useful for code that is not deterministic, like random numbers.
    python_interactive_no_check: bool = False

    # {no-print}
    # This flag removes any output done by print() or other functions
    # of the code block.
    # Usually useful for any code that prints something.
    no_print: bool = False

    # {ipython-native}
    # This flag enables ipython magic but for the price,
    # see IPythonExecutor.
    ipython_native: bool = False

    # {shield:ExceptionType}
    # This flag allows the code to raise ExceptionType.
    shield: str | None = None

    _MAP_TAGS_TO_ATTRS = {
        'hide': 'hide',
        'continue': 'continue_code',
        'merge': 'merge',
        'no-run': 'no_run',
        'python-interactive-no-check': 'python_interactive_no_check',
        'no-print': 'no_print',
        'ipython-native': 'ipython_native',
        'shield': 'shield',
    }

    def __post_init__(self) -> None:
        if self.merge and not self.continue_code:
            raise ValueError('Cannot {merge} without {continue}')
        if self.ipython_native and not self.is_ipython:
            raise ValueError('ipython-native is only allowed for ipython code')
        if self.python_interactive_no_check and not self.is_python_interactive:
            raise ValueError(
                'python-interactive-no-check is only allowed for python interactive code'
            )

    @cached_property
    def is_python(self) -> bool:
        return Language.PYTHON == self.language

    @cached_property
    def is_python_interactive(self) -> bool:
        return Language.PYTHON_INTERACTIVE == self.language

    @cached_property
    def is_ipython(self) -> bool:
        return Language.IPYTHON == self.language

    @classmethod
    def from_token(cls, token: markdown_it.token.Token) -> ParagraphCode:
        assert token.type == 'fence'

        words = token.info.split()
        language = ''
        kwargs: dict[str, Any] = {}

        first_word: bool = True
        in_comment: bool = False
        for word in words:
            if '{' != word[0] or '}' != word[-1]:
                if word.startswith('{#'):
                    in_comment = True
                if in_comment:
                    # no nested comments
                    if word.endswith('#}'):
                        in_comment = False
                    continue

                if first_word:
                    language = word
                    continue
                else:
                    raise ValueError(f'Invalid tag: {word}, should be {{tag}}')

            tag_name: str
            tag_value: Any
            if ':' in word:
                tag_name, tag_value = word[1:-1].split(':', 1)
            else:
                tag_name, tag_value = word[1:-1], True

            if tag_name in cls._MAP_TAGS_TO_ATTRS:
                kwargs[cls._MAP_TAGS_TO_ATTRS[tag_name]] = tag_value
            else:
                raise ValueError(f'Invalid tag: {word}')

            first_word = False

        return cls(
            body=token.content,
            language=Language(language),
            **kwargs,
        )


@dataclasses.dataclass
class Paragraph:
    tokens: list[markdown_it.token.Token]
    code: ParagraphCode | None = None


class PostMarkdown:
    def __init__(self, text):
        self.text = text
        self._parser = MarkdownIt()

    def copy(self) -> 'PostMarkdown':
        return PostMarkdown(self.text)

    def has_header(self) -> bool:
        return self.text.strip().startswith('# ')

    def has_empty_line_bof(self) -> bool:
        return self.text.startswith('\n\n#')

    def has_empty_line_eof(self) -> bool:
        return self.text.endswith('\n')

    def has_images(self) -> bool:
        queue = self._parser.parse(self.text)
        while queue:
            token = queue.pop(0)
            if token.type == 'image':
                return True
            if token.type == 'inline':
                if token.children:
                    queue.extend(token.children)

        return False

    def title(self) -> str:
        first_line = self.text.lstrip().split('\n', maxsplit=1)[0]
        if first_line.startswith('# '):
            first_line = first_line[2:]
        return first_line

    def content(self) -> str:
        return self.text.lstrip().split('\n', maxsplit=1)[-1]

    def html_content(self) -> str:
        self._remove_hidden_code_blocks()
        self._merge_code_blocks()
        return self._parser.render(self.text)

    def html_content_no_header(self) -> str:
        self._remove_hidden_code_blocks()
        self._merge_code_blocks()
        self._remove_header()
        return self.html_content()

    def to_telegram(self) -> None:
        self.run_code()
        self._remove_header()
        self._remove_hidden_code_blocks()
        self._merge_code_blocks()
        self._remove_code_info()

    def run_code(self) -> None:
        shared_globals: dict = {}
        for paragraph in self._paragraphs():

            if (
                paragraph.code is None
                or paragraph.code.no_run
                or not (
                    paragraph.code.is_python
                    or paragraph.code.is_python_interactive
                    or paragraph.code.is_ipython
                )
            ):
                continue

            if not paragraph.code.continue_code:
                shared_globals = {}
            shared_globals['print'] = (
                (lambda *args, **kwargs: None)
                if paragraph.code.no_print
                else print
            )

            code = paragraph.tokens[-1].content
            if paragraph.code.is_python:
                if paragraph.code.shield:
                    raise NotImplementedError()
                exec(code, shared_globals)
            if paragraph.code.is_python_interactive:
                self._exec_cli(
                    code, shared_globals,
                    check_interactive=not paragraph.code.python_interactive_no_check,
                    shield=paragraph.code.shield,
                )
            if paragraph.code.is_ipython:
                self._exec_ipython(
                    code,
                    shared_globals,
                    shield=paragraph.code.shield,
                    native=paragraph.code.ipython_native,
                )

    def _exec_cli(
        self, code: str, shared_globals: dict, shield: str | None = None,
        *,
        check_interactive: bool,
    ) -> None:
        in_out: list[tuple[str, str]] = []
        for line in code.splitlines():
            if line.startswith('>>> '):
                in_out.append((line[4:], ''))
            elif line.startswith('...'):
                in_out[-1] = (in_out[-1][0] + line[4:], '')
            else:
                in_out[-1] = (in_out[-1][0], in_out[-1][1] + line)

        for in_, out in in_out:
            result = eval_or_exec(in_, shared_globals=shared_globals, shield=shield)
            if check_interactive:
                assert str(result) == out, f'`{result}` != `{out}`'

    def _exec_ipython(
        self,
        code: str,
        shared_globals: dict,
        shield: str | None,
        native: bool,
    ) -> None:
        executor = IPythonExecutor(code, shield=shield, native=native)
        commands: list[IPythonCommand] = list(executor.run(shared_globals))

        for command in commands:
            assert command.out == command.real_out, \
                f'`{command.out}` != `{command.real_out}`'

    def _remove_code_info(self) -> None:
        lines = self.text.splitlines(keepends=True)
        for token in self._parser.parse(self.text):
            if token.type == 'fence':
                assert token.map
                line_number = token.map[0]
                lines[line_number] = '```\n'

        self.text = ''.join(lines)

    def _remove_header(self) -> None:
        if self.has_header():
            self.text = self.text.lstrip().split('\n', maxsplit=1)[-1].lstrip()

    def _remove_hidden_code_blocks(self) -> None:
        result = self.text.splitlines(keepends=True)

        shift = 0
        for p in self._paragraphs():
            if p.code and p.code.hide:
                for token in p.tokens:
                    if not token.map:
                        continue
                    first_line, until_line = token.map
                    lineno = until_line - shift
                    if lineno < len(result) and result[lineno] == '\n':
                        # remove empty line after hidden paragraph
                        until_line += 1
                    result = result[:first_line - shift] + result[until_line - shift:]
                    shift += until_line - first_line
                    break

        self.text = ''.join(result)

    def _merge_code_blocks(self) -> None:
        result = self.text.splitlines(keepends=True)

        shift = 0
        prev_code_map = None
        for p in self._paragraphs():
            if p.code:
                if p.code.merge:
                    if prev_code_map is None:
                        raise ValueError(
                            'Code block can not be merged with previous non-code block'
                        )
                    for token in p.tokens:
                        if not token.map:
                            continue
                        first_line, _ = token.map
                        _, prev_until_line = prev_code_map

                        result = (
                            result[:prev_until_line - shift - 1]
                            + result[first_line - shift + 1:]
                        )
                        shift += first_line - prev_until_line + 2
                        break
                else:
                    for token in p.tokens:
                        if not token.map:
                            continue
                        prev_code_map = token.map
                        break
            else:
                prev_code_map = None

        self.text = ''.join(result)

    def _paragraphs(self) -> Iterator[Paragraph]:
        paragraph_tokens = []
        paragraph_depth: int = 0
        for token in self._parser.parse(self.text):
            if paragraph_depth > 0:
                if token.type.endswith('_open'):
                    paragraph_depth += 1
                elif token.type.endswith('_close'):
                    paragraph_depth -= 1
                if paragraph_depth == 0:
                    # Only yield top-level paragraphs
                    paragraph_tokens.append(token)
                    yield Paragraph(tokens=paragraph_tokens)
                    paragraph_tokens = []
                else:
                    paragraph_tokens.append(token)
            else:
                if token.type.endswith('_open'):
                    paragraph_tokens = [token]
                    paragraph_depth += 1
                elif token.type.endswith('_close'):
                    raise ValueError('unexpected paragraph close')
                else:
                    if token.type == 'fence':
                        code = ParagraphCode.from_token(token)
                        yield Paragraph(tokens=[token], code=code)
                    else:
                        yield Paragraph(tokens=[token])
