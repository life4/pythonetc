from __future__ import annotations
from dataclasses import dataclass, field
from functools import cached_property, lru_cache
from pathlib import Path
from typing import TYPE_CHECKING
import requests

if TYPE_CHECKING:
    from .post import Post


CACHE = Path(__file__).parent.parent / 'peps'


@dataclass
class PEP:
    rst: str
    posts: list[Post] = field(default_factory=list)

    @cached_property
    def number(self) -> int:
        for line in self.rst.splitlines():
            if line.startswith('PEP: '):
                return int(line.removeprefix('PEP: ').strip())
        raise LookupError

    @cached_property
    def slug(self) -> str:
        return f'pep-{self.number:04}'

    @cached_property
    def title(self) -> str:
        for line in self.rst.splitlines():
            if line.startswith('Title: '):
                return line.removeprefix('Title: ').strip()
        raise LookupError

    @property
    def url(self) -> str:
        return f'https://peps.python.org/{self.slug}/'


@lru_cache
def get_pep(number: int) -> PEP:
    name = f'pep-{number:04}'
    path = CACHE / f'{name}.rst'
    if path.exists():
        rst = path.read_text(encoding='utf8')
        return PEP(rst=rst)
    url = f'https://raw.githubusercontent.com/python/peps/main/{name}.rst'
    resp = requests.get(url)
    if resp.status_code == 404:
        url = f'https://raw.githubusercontent.com/python/peps/main/{name}.txt'
        resp = requests.get(url)
    resp.raise_for_status()
    rst = resp.text
    CACHE.mkdir(exist_ok=True)
    path.write_text(rst, encoding='utf8')
    return PEP(rst=rst)
