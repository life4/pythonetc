from __future__ import annotations
from datetime import date
from functools import cached_property
import json
from pathlib import Path
import re
import attr
import yaml
import jsonschema
from markdown_it import MarkdownIt
from .pep import get_pep, PEP
from .trace import Trace, parse_traces

md_parser = MarkdownIt()
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
    posts.sort(key=lambda post: post.published or date.today())
    return posts


@attr.s(auto_attribs=True, frozen=True)
class Post:
    path: Path
    markdown: str
    author: str
    id: int | None = None
    traces: list[Trace] = attr.ib(factory=list, converter=parse_traces)
    pep: int | None = None
    topics: list[str] = attr.ib(factory=list)
    published: date | None = None
    python: str | None = None

    @classmethod
    def from_path(cls, path: Path) -> Post:
        yaml_str, markdown = path.read_text('utf8').lstrip().split('\n---', 1)
        meta: dict = yaml.safe_load(yaml_str)
        try:
            jsonschema.validate(meta, SCHEMA)
        except jsonschema.ValidationError:
            raise ValueError(f'invalid metadata for {path.name}')
        return cls(**meta, path=path, markdown=markdown)

    def validate(self) -> str | None:
        if not REX_FILE_NAME.fullmatch(self.path.name):
            return 'file name must be kebab-case'
        if not self.markdown.strip().startswith('# '):
            return 'header is required'
        if not self.markdown.endswith('\n'):
            return 'empty line at the end of the file is required'
        if self.id and not self.published:
            return 'posts with `id` must also have `published`'
        return None

    @cached_property
    def title(self) -> str:
        first_line = self.markdown.lstrip().split('\n', maxsplit=1)[0]
        if first_line.startswith('# '):
            first_line = first_line[2:]
        return first_line

    @cached_property
    def md_content(self) -> str:
        return self.markdown.lstrip().split('\n', maxsplit=1)[-1]

    @cached_property
    def html_content(self) -> str:
        return md_parser.render(self.md_content)

    @property
    def slug(self) -> str:
        return self.path.stem

    @property
    def url(self) -> str:
        return f'posts/{self.slug}.html'

    @cached_property
    def pep_info(self) -> PEP | None:
        if self.pep is None:
            return None
        pep = get_pep(self.pep)
        pep.posts.append(self)
        return pep

    @cached_property
    def telegram_markdown(self) -> str:
        lines = self.markdown.splitlines(keepends=True)
        for token in md_parser.parse(self.markdown):
            if token.type == 'fence':
                assert token.map
                line_number = token.map[0]
                lines[line_number] = '```\n'
        return ''.join(lines)
