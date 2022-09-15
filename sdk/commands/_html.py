
from __future__ import annotations

from pathlib import Path
from ._command import Command
from ..pep import PEP
from ..post import Post, get_posts
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent.parent.parent
TEMPLATES_PATH = ROOT / 'templates'
jinja_env = Environment(
    loader=FileSystemLoader(TEMPLATES_PATH),
)


class HTMLCommand(Command):
    """Generate static HTML pages.
    """
    name = 'html'

    def run(self) -> int:
        posts = get_posts()
        (ROOT / 'public' / 'posts').mkdir(exist_ok=True, parents=True)
        render_html('index')
        render_html('posts', posts=posts, title='all posts')
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
        modules: list[Post] = []
        for post in posts:
            if 'module' in post.topics and 'stdlib' in post.topics:
                modules.append(post)
        modules.sort(key=lambda p: p.module_name or '')
        render_html(
            'stdlib',
            posts=modules,
            title='stdlib',
        )

        for post in posts:
            render_post(post)
        return 0


def render_html(slug: str, **kwargs) -> None:
    print(slug)
    template = jinja_env.get_template(f'{slug}.html.j2')
    content = template.render(len=len, **kwargs)
    html_path = ROOT / 'public' / f'{slug}.html'
    html_path.write_text(content, encoding='utf8')


def render_post(post: Post) -> None:
    print(f'posts/{post.slug}')
    template = jinja_env.get_template('post.html.j2')
    content = template.render(post=post, title=post.title)
    html_path = ROOT / 'public' / 'posts' / f'{post.slug}.html'
    html_path.write_text(content, encoding='utf8')
