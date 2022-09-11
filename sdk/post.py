from __future__ import annotations
from datetime import date
from functools import cached_property
from pathlib import Path
import attr
import yaml
from markdown_it import MarkdownIt
from .pep import get_pep, PEP

md_parser = MarkdownIt()


def wrap_list(x: object) -> list:
    if isinstance(x, list):
        return x
    return [x]


@attr.s(auto_attribs=True, frozen=True)
class Post:
    path: Path
    markdown: str
    author: str
    id: int | None = None
    qname: list[str] = attr.ib(factory=list, converter=wrap_list)
    pep: list[int] = attr.ib(factory=list, converter=wrap_list)
    published: date | None = None
    python: str | None = None

    @classmethod
    def from_path(cls, path: Path) -> Post:
        yaml_str, markdown = path.read_text().lstrip().split('\n---', 1)
        meta: dict = yaml.safe_load(yaml_str)
        qname = meta.setdefault('qname', [])
        if isinstance(meta['qname'], str):
            meta['qname'] = [qname]
        return cls(**meta, path=path, markdown=markdown)

    @cached_property
    def title(self) -> str:
        first_line = self.markdown.lstrip().split('\n', maxsplit=1)[0]
        return first_line.removeprefix('# ')

    @cached_property
    def md_content(self) -> str:
        return self.markdown.lstrip().split('\n', maxsplit=1)[-1]

    @cached_property
    def html_content(self) -> str:
        return md_parser.render(self.md_content)

    @property
    def slug(self) -> str:
        return self.path.stem

    @cached_property
    def peps(self) -> list[PEP]:
        peps = []
        for pep_number in self.pep:
            pep = get_pep(pep_number)
            pep.posts.append(self)
            peps.append(pep)
        return peps
