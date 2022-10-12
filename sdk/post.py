from __future__ import annotations
from dataclasses import dataclass, field

import json
import re
from datetime import date
from functools import cached_property
from pathlib import Path

import jsonschema
import yaml

from sdk.post_markdown import PostMarkdown

from .pep import PEP, get_pep
from .trace import Trace, parse_traces


SCHEMA_PATH = Path(__file__).parent / 'schema.json'
SCHEMA = json.loads(SCHEMA_PATH.read_text())
REX_FILE_NAME = re.compile(r'[a-z0-9-]+\.md')
ROOT = Path(__file__).parent.parent


def get_posts() -> list[Post]:
    posts: list[Post] = []
    posts_path = ROOT / 'posts'
    for path in posts_path.iterdir():
        if path.suffix != '.md':
            continue
        post = Post.from_path(path)
        error = post.validate()
        if error:
            raise ValueError(f'invalid {post.path.name}: {error}')
        posts.append(post)
    posts.sort()
    return posts


@dataclass(frozen=True)
class PostChain:
    name: str
    idx: int
    length: int
    prev: int | None
    next: int | None
    delay_allowed: bool = False


@dataclass(frozen=True)
class Post:
    path: Path
    markdown: PostMarkdown
    author: str
    id: int | None = None
    traces: list[Trace] = field(default_factory=list)
    pep: int | None = None
    topics: list[str] = field(default_factory=list)
    depends_on: list[str] = field(default_factory=list)
    published: date | None = None
    python: str | None = None
    chain: PostChain | None = None

    @classmethod
    def from_path(cls, path: Path) -> Post:
        yaml_str, markdown = path.read_text('utf8').lstrip().split('\n---', 1)
        meta: dict = yaml.safe_load(yaml_str)
        try:
            jsonschema.validate(meta, SCHEMA)
        except jsonschema.ValidationError:
            raise ValueError(f'invalid metadata for {path.name}')

        chain: PostChain | None = None
        if 'chain' in meta:
            chain = PostChain(**meta.pop('chain'))
        traces: list[Trace] = []
        if 'traces' in meta:
            traces = parse_traces(meta.pop('traces'))

        return cls(
            **meta,
            chain=chain,
            path=path,
            traces=traces,
            markdown=PostMarkdown(markdown),
        )

    def validate(self) -> str | None:
        if not REX_FILE_NAME.fullmatch(self.path.name):
            return 'file name must be kebab-case'
        if not self.markdown.has_header():
            return 'header is required'
        if not self.markdown.has_empty_line_bof():
            return 'empty line at the beginning of the file is required'
        if not self.markdown.has_empty_line_eof():
            return 'empty line at the end of the file is required'
        if self.id and not self.published:
            return 'posts with `id` must also have `published`'
        return None

    def run_code(self) -> None:
        self.markdown.run_code()

    @cached_property
    def title(self) -> str:
        return self.markdown.title()

    @cached_property
    def md_content(self) -> str:
        return self.markdown.content()

    @cached_property
    def html_content(self) -> str:
        return self.markdown.html_content()

    @property
    def slug(self) -> str:
        return self.path.stem

    @property
    def url(self) -> str:
        return f'posts/{self.slug}.html'

    @property
    def is_typing(self) -> bool:
        if 'typing' in self.topics:
            return True
        return any(trace.module_name == 'typing' for trace in self.traces)

    @cached_property
    def pep_info(self) -> PEP | None:
        if self.pep is None:
            return None
        pep = get_pep(self.pep)
        pep.posts.append(self)
        return pep

    @cached_property
    def telegram_markdown(self) -> str:
        copy = self.markdown.copy()
        copy.to_telegram()

        return copy.text

    def __lt__(self, other: Post) -> bool:
        date1 = self.published or date.today()
        date2 = other.published or date.today()
        return (date1, self.path.name) < (date2, other.path.name)
