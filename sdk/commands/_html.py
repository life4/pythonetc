from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Optional

import jinja2

from ..module import Module
from ..pages import PAGES
from ..pep import PEP
from ..post import Post, get_posts
from ._command import Command


ROOT = Path(__file__).parent.parent.parent
TEMPLATES_PATH = ROOT / 'templates'
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    undefined=jinja2.StrictUndefined,
)


@dataclass(frozen=True)
class PostToRender(Post):
    other_posts_in_sequence: list[Post] = field(default_factory=list)

    @classmethod
    def from_post(cls, post: Post) -> PostToRender:
        other_posts_in_sequence = []
        if post.sequence:
            other_posts_in_sequence = [
                p for p in post.sequence.posts
                if p.path.absolute() != post.path.absolute()
            ]

        return cls(other_posts_in_sequence=other_posts_in_sequence, **post.__dict__)


class HTMLCommand(Command):
    """Generate static HTML pages.
    """
    name = 'html'

    def run(self) -> int:
        all_posts = get_posts()
        posts = [
            PostToRender.from_post(post)
            for post in all_posts
            if post.first_in_sequence()
        ]
        (ROOT / 'public' / 'posts').mkdir(exist_ok=True, parents=True)

        years: defaultdict[int, list[Post]] = defaultdict(list)
        today = date.today()
        for post in posts:
            published = post.published or today
            years[published.year].append(post)
        render_html('index', pages=PAGES, years=sorted(years.items()))
        render_html('typing', posts=posts, title='typing')

        pythons = sorted(
            {post.python for post in posts if post.python},
            key=lambda p: int(p.split('.')[-1]),
        )
        render_html(
            'pythons',
            posts=posts,
            pythons=pythons,
            title='python changelog',
        )

        peps: dict[int, PEP] = {}
        for post in posts:
            pep = post.pep_info
            if pep is not None:
                peps[pep.number] = pep
        peps_list = sorted(peps.items())
        render_html(
            'peps',
            peps=[pep for _, pep in peps_list],
            title='PEPs',
        )

        render_html(
            'stdlib',
            modules=Module.from_posts(posts),
            title='stdlib',
        )

        for post in posts:
            if post.sequence is not None and post.first_in_sequence():
                posts_in_sequence = [p for p in all_posts if p.sequence == post.sequence]
                render_post(post, all_posts=posts_in_sequence)
            else:
                render_post(post)

        return 0


def render_html(slug: str, title: str | None = None, **kwargs) -> None:
    template = jinja_env.get_template(f'{slug}.html.j2')
    content = template.render(len=len, title=title, **kwargs)
    html_path = ROOT / 'public' / f'{slug}.html'
    html_path.write_text(content, encoding='utf8')


def render_post(post: Post, *, all_posts: Optional[list[Post]] = None) -> None:
    if all_posts is None:
        all_posts = [post]

    template = jinja_env.get_template('post.html.j2')
    content = template.render(post=post, title=post.title, other_posts=all_posts)
    html_path = ROOT / 'public' / 'posts' / f'{post.slug}.html'
    html_path.write_text(content, encoding='utf8')
