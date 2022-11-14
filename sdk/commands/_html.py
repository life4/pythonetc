from __future__ import annotations

import shutil
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import jinja2

from ..module import Module
from ..pages import PAGES
from ..pep import PEP
from ..post import Post, get_posts
from ..sequence import PostOfSequence
from ._command import Command


ROOT = Path(__file__).parent.parent.parent
TEMPLATES_PATH = ROOT / 'templates'
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
    undefined=jinja2.StrictUndefined,
)


@dataclass(frozen=True)
class PostToRender(Post):
    other_posts_in_sequence: list[PostOfSequence] = field(default_factory=list)
    stick_to_previous: bool = False

    @classmethod
    def from_post(cls, post: Post) -> PostToRender:
        other_posts_in_sequence = []
        if post.sequence:
            other_posts_in_sequence = [
                p for p in post.sequence.posts
                if p.path.absolute() != post.path.absolute()
            ]

        stick_to_previous = False
        self_in_sequence = post.self_in_sequence()
        if (
            not post.first_in_sequence()
            and self_in_sequence is not None
            and not self_in_sequence.delay_allowed
        ):
            stick_to_previous = True

        return cls(
            stick_to_previous=stick_to_previous,
            other_posts_in_sequence=other_posts_in_sequence,
            **post.__dict__,
        )


class HTMLCommand(Command):
    """Generate static HTML pages.
    """
    name = 'html'

    def run(self) -> int:
        all_posts: dict[Path, Post] = get_posts()
        all_posts_to_render: dict[Path, PostToRender] = {
            path: PostToRender.from_post(post)
            for path, post in all_posts.items()
        }
        posts: list[PostToRender] = [
            p for p in all_posts_to_render.values()
            if p.first_in_sequence()
        ]

        self._prepare_dirs()

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
                posts_in_sequence: list[PostToRender] = [
                    all_posts_to_render[post_in_sequence.path.absolute()]
                    for post_in_sequence in post.sequence.posts
                ]
                render_post(posts=posts_in_sequence)
            else:
                render_post(posts=[post])

        return 0

    def _prepare_dirs(self) -> None:
        posts = ROOT / 'public' / 'posts'
        posts.mkdir(exist_ok=True, parents=True)

        img = ROOT / 'public' / 'posts' / 'img'
        shutil.rmtree(img, ignore_errors=True)

        shutil.copytree(ROOT / 'posts' / 'img', ROOT / 'public' / 'posts' / 'img')


def render_html(slug: str, title: str | None = None, **kwargs) -> None:
    template = jinja_env.get_template(f'{slug}.html.j2')
    content = template.render(len=len, title=title, **kwargs)
    html_path = ROOT / 'public' / f'{slug}.html'
    html_path.write_text(content, encoding='utf8')


def render_post(posts: list[PostToRender]) -> None:
    main_post = posts[0]
    template = jinja_env.get_template('post.html.j2')
    content = template.render(title=main_post.title, posts=posts)
    html_path = ROOT / 'public' / 'posts' / f'{main_post.slug}.html'
    html_path.write_text(content, encoding='utf8')
