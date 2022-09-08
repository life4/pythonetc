from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from functools import cached_property
from pathlib import Path
import yaml


@dataclass(frozen=True)
class Post:
    path: Path
    markdown: str
    author: str
    qname: list[str]
    published: date | None = None
    pep: int | None = None
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
