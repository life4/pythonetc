from __future__ import annotations

import dataclasses
import enum
from functools import cached_property
from pathlib import Path
from types import MappingProxyType
from typing import Any, Iterator, Mapping

import markdown_it.token
from markdown_it import MarkdownIt

from sdk.ipython_executor import IPythonCommand, IPythonExecutor
from sdk.python_exec_utils import eval_or_exec


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
_DEFAULT_GLOBALS: Mapping[str, object] = MappingProxyType(dict(
    reveal_type=lambda x: x,
))


class Language(str, enum.Enum):
    NONE = ''
    PYTHON = 'python'
    PYTHON_INTERACTIVE = 'python-interactive'
    IPYTHON = 'ipython'
    TEXT = 'text'
    BASH = 'bash'
    SQL = 'sql'
    JS = 'js'
    GO = 'go'
    HASKELL = 'haskell'
    TOML = 'toml'


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

    def __post_init__(self) -> None:
        if self.merge and not self.continue_code:
            raise ValueError('Cannot {merge} without {continue}')
        if self.ipython_native and not self.is_ipython:
            raise ValueError('ipython-native is only allowed for ipython code')
        if (
            self.python_interactive_no_check
            and not (self.is_python_interactive or self.is_ipython)
        ):
            raise ValueError(
                'python-interactive-no-check is only allowed for python interactive code',
            )

    @cached_property
    def is_python(self) -> bool:
        return self.language == Language.PYTHON

    @cached_property
    def is_python_interactive(self) -> bool:
        return self.language == Language.PYTHON_INTERACTIVE

    @cached_property
    def is_ipython(self) -> bool:
        return self.language == Language.IPYTHON

    @classmethod
    def from_token(cls, token: markdown_it.token.Token) -> ParagraphCode:
        assert token.type == 'fence'

        words = token.info.split()
        language = ''
        kwargs: dict[str, Any] = {}

        first_word: bool = True
        in_comment: bool = False
        for word in words:
            if word[0] != '{' or word[-1] != '}':
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

            if tag_name in _MAP_TAGS_TO_ATTRS:
                kwargs[_MAP_TAGS_TO_ATTRS[tag_name]] = tag_value
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


@dataclasses.dataclass
class PostMarkdown:
    text: str
    path: Path | None = None
    _parser: MarkdownIt = dataclasses.field(default_factory=MarkdownIt)

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
            if token.type == 'inline' and token.children:
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
        self._rename_languages()
        return self._parser.render(self.text)

    def html_content_no_header(self) -> str:
        self._remove_hidden_code_blocks()
        self._merge_code_blocks()
        self._rename_languages()
        self._remove_header()
        return self.html_content()

    def to_telegram(self) -> None:
        self.run_code()
        self._remove_header()
        self._remove_hidden_code_blocks()
        self._merge_code_blocks()
        self._remove_code_info()

    def run_code(self) -> None:
        shared_globals: dict[str, object] = dict(_DEFAULT_GLOBALS)
        for paragraph in self._paragraphs():
            if paragraph.code is None or paragraph.code.no_run:
                continue
            if not (
                paragraph.code.is_python
                or paragraph.code.is_python_interactive
                or paragraph.code.is_ipython
            ):
                continue
            if not paragraph.code.continue_code:
                shared_globals = dict(_DEFAULT_GLOBALS)
            if paragraph.code.no_print:
                shared_globals['print'] = lambda *args, **kwargs: None
            else:
                shared_globals['print'] = print
            raw_code = paragraph.tokens[-1].content
            try:
                self._run_paragraph(raw_code, paragraph.code, shared_globals)
            except BaseException as exc:
                lineno = self._get_lineno(raw_code)
                if lineno is not None:
                    exc.add_note(f'Error occured in code block on line {lineno}')
                if paragraph.code.shield:
                    exc.add_note(f'Expected exception: {paragraph.code.shield}')
                raise

    def _run_paragraph(
        self,
        raw_code: str,
        par_code: ParagraphCode,
        shared_globals: dict[str, object],
    ) -> None:
        if par_code.is_python:
            eval_or_exec(
                raw_code,
                shared_globals=shared_globals,
                shield=par_code.shield,
            )
            return
        if par_code.is_python_interactive:
            self._exec_cli(
                raw_code, shared_globals,
                check_interactive=not par_code.python_interactive_no_check,
                shield=par_code.shield,
            )
            return
        if par_code.is_ipython:
            self._exec_ipython(
                raw_code,
                shared_globals,
                check_interactive=not par_code.python_interactive_no_check,
                shield=par_code.shield,
                native=par_code.ipython_native,
            )
            return

    def _get_lineno(self, raw_code: str) -> int | None:
        """Given raw code block, find its line number in the original file.
        """
        if self.path is None:
            return None
        post_content = self.path.read_text()
        if post_content.count(raw_code) != 1:
            return None
        pos = post_content.find(raw_code)
        if pos == -1:
            return None
        text_before = post_content[:pos]
        return text_before.count('\n')

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
        check_interactive: bool,
        shield: str | None,
        native: bool,
    ) -> None:
        executor = IPythonExecutor(code, shield=shield, native=native)
        commands: list[IPythonCommand] = list(executor.run(shared_globals))

        if check_interactive:
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
                            'Code block can not be merged with previous non-code block',
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

    def _rename_languages(self) -> None:
        rules = {
            Language.IPYTHON: 'python',
            Language.PYTHON_INTERACTIVE: 'python',
        }

        result = self.text.splitlines(keepends=True)
        for p in self._paragraphs():
            if p.code and p.code.language in rules:
                for token in p.tokens:
                    if not token.map:
                        continue

                    first_line, until_line = token.map
                    result[first_line] = result[first_line].replace(
                        '```' + p.code.language,
                        '```' + rules[p.code.language],
                    )

                    break

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
            elif token.type.endswith('_open'):
                paragraph_tokens = [token]
                paragraph_depth += 1
            elif token.type.endswith('_close'):
                raise ValueError('unexpected paragraph close')
            elif token.type == 'fence':
                code = ParagraphCode.from_token(token)
                yield Paragraph(tokens=[token], code=code)
            else:
                yield Paragraph(tokens=[token])
