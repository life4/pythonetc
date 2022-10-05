from __future__ import annotations

import dataclasses
from functools import cached_property
from typing import Iterator

import markdown_it.token
from markdown_it import MarkdownIt


@dataclasses.dataclass
class ParagraphCode:
    body: str
    info: list[str]
    skip: bool
    continue_code: bool

    @cached_property
    def is_python(self) -> bool:
        return 'python' in self.info

    @cached_property
    def is_python_cli(self) -> bool:
        return 'python-cli' in self.info


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

    def has_empty_line_eof(self) -> bool:
        return self.text.endswith('\n')

    def title(self) -> str:
        first_line = self.text.lstrip().split('\n', maxsplit=1)[0]
        if first_line.startswith('# '):
            first_line = first_line[2:]
        return first_line

    def content(self) -> str:
        return self.text.lstrip().split('\n', maxsplit=1)[-1]

    def html_content(self) -> str:
        return self._parser.render(self.text)

    def to_telegram(self) -> None:
        self.run_code()
        self._skipped_removed()
        self._remove_code_info()

    def run_code(self) -> None:
        shared_globals = {}
        for paragraph in self._paragraphs():
            if (
                paragraph.code is None or not (
                    paragraph.code.is_python or paragraph.code.is_python_cli
                )
            ):
                continue

            if not paragraph.code.continue_code:
                shared_globals = {}

            code = paragraph.tokens[-1].content
            if paragraph.code.is_python:
                exec(code, shared_globals)
            if paragraph.code.is_python_cli:
                self._exec_cli(code, shared_globals)

    def _exec_cli(self, code: str, shared_globals: dict) -> None:
        in_out: list[tuple[str, str]] = []
        for line in code.splitlines():
            if line.startswith('>>> '):
                in_out.append((line[4:], ''))
            elif line.startswith('... '):
                in_out[-1] = (in_out[-1][0] + line[4:], '')
            else:
                in_out[-1] = (in_out[-1][0], in_out[-1][1] + line)

        for in_, out in in_out:
            result = eval(in_, shared_globals)
            assert str(result) == out, f'{result} != {out}'

    def _remove_code_info(self) -> None:
        lines = self.text.splitlines(keepends=True)
        for token in self._parser.parse(self.text):
            info = set(token.info.split(','))
            if 'skip' in info:
                continue
            if token.type == 'fence':
                assert token.map
                line_number = token.map[0]
                lines[line_number] = '```\n'

        self.text = ''.join(lines)

    def _skipped_removed(self) -> None:
        result = self.text.splitlines(keepends=True)

        shift = 0
        for p in self._paragraphs():
            if p.code and p.code.skip:
                for token in p.tokens:
                    if not token.map:
                        continue
                    first_line, until_line = token.map
                    lineno = until_line - shift
                    if lineno < len(result) and result[lineno] == '\n':
                        # remove empty line after skipped paragraph
                        until_line += 1
                    result = result[:first_line - shift] + result[until_line - shift:]
                    shift += until_line - first_line

        self.text = ''.join(result)

    def _paragraphs(self) -> Iterator[Paragraph]:
        paragraph_tokens = []
        in_paragraph = False
        for token in self._parser.parse(self.text):
            if in_paragraph:
                if token.type.endswith('_open'):
                    raise ValueError('nested paragraphs')
                elif token.type.endswith('_close'):
                    paragraph_tokens.append(token)
                    yield Paragraph(tokens=paragraph_tokens)
                    paragraph_tokens = []
                    in_paragraph = False
                else:
                    paragraph_tokens.append(token)
            else:
                if token.type.endswith('_open'):
                    paragraph_tokens = [token]
                    in_paragraph = True
                elif token.type.endswith('_close'):
                    raise ValueError('unexpected paragraph close')
                else:
                    if token.type == 'fence':
                        info = token.info.split(' ')
                        code = ParagraphCode(
                            body=token.content,
                            info=info,
                            skip='{skip}' in info,
                            continue_code='{continue}' in info,
                        )
                        yield Paragraph(tokens=[token], code=code)
                    else:
                        yield Paragraph(tokens=[token])
