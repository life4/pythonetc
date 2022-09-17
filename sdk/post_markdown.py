import dataclasses
from typing import Generator, Iterator

import markdown_it.token
from markdown_it import MarkdownIt


@dataclasses.dataclass
class Paragraph:
    tokens: list[markdown_it.token.Token]


@dataclasses.dataclass
class ParagraphWithBangSupport:
    tokens: list[markdown_it.token.Token]
    bang_annotations: list[str] = dataclasses.field(default_factory=list)


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
        code = ''
        for paragraph in self._paragraphs_with_bang_support():
            if not paragraph.tokens[-1].type == 'fence':
                continue

            if 'continue' not in paragraph.bang_annotations:
                if code:
                    exec(code)
                code = ''

            code += paragraph.tokens[-1].content

        exec(code)

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
        for b in self._paragraphs_with_bang_support():
            if 'skip' in b.bang_annotations:
                for token in b.tokens:
                    if not token.map:
                        continue
                    first_line, until_line = token.map
                    result = result[:first_line - shift] + result[until_line - shift:]
                    shift += until_line - first_line

        self.text = ''.join(result)

    def _paragraphs_with_bang_support(self) -> Iterator[ParagraphWithBangSupport]:
        """
        Lines started with '!' are special kind of home-brewed annotations.
        They are removed from the output, but they control how the next paragraph is rendered.
        """
        bang_annotation_paragraphs: list[Paragraph] = []
        paragraph: Paragraph
        for paragraph in self._paragraphs():
            if (
                len(paragraph.tokens) == 3 and
                paragraph.tokens[0].type.endswith('_open') and
                paragraph.tokens[1].type == 'inline' and
                paragraph.tokens[2].type.endswith('_close') and
                paragraph.tokens[1].content.startswith('!')
            ):
                bang_annotation_paragraphs.append(paragraph)
            else:
                tokens = []
                for b in bang_annotation_paragraphs:
                    tokens.extend(b.tokens)
                yield ParagraphWithBangSupport(
                    tokens=tokens + paragraph.tokens,
                    bang_annotations=[
                        s.strip()
                        for b in bang_annotation_paragraphs
                        for s in b.tokens[1].content.removeprefix('!').split(',')
                    ],
                )
                bang_annotation_paragraphs = []  # reset

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
                    yield Paragraph(tokens=[token])
