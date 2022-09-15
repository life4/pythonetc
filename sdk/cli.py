from __future__ import annotations

import argparse
from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import sys
from typing import Callable, Mapping, NoReturn, TextIO

from .post import Post
from .pep import PEP
from jinja2 import Environment, FileSystemLoader

try:
    import ipdb as pdb
except ImportError:
    import pdb  # type: ignore

Command = Callable[[argparse.Namespace], int]
ROOT = Path(__file__).parent.parent
TEMPLATES_PATH = ROOT / 'templates'
jinja_env = Environment(
    loader=FileSystemLoader(TEMPLATES_PATH),
)
TITLES = {
    'index.html': 'Python etc.',
    # 'peps.html': 'Python etc. / PEPs',
    'peps.html': 'Python etc. / PEPs',
}


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


def cmd_table(args: argparse.Namespace) -> int:
    for post in get_posts():
        pep = f'PEP {post.pep:<4}' if post.pep else ' ' * 8
        python = f'{post.python:<4}' if post.python else ' ' * 4
        print(f'{post.published} | {pep} | {python} | {post.title}')
    return 0


def cmd_html(args: argparse.Namespace) -> int:
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


def cmd_telegram(args: argparse.Namespace) -> int:
    assert args.post is not None, "--post is required"

    print(Post.from_path(ROOT / 'posts' / f'{args.post}.md').telegram_markdown)

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


COMMANDS: Mapping[str, Command] = {
    'table': cmd_table,
    'html': cmd_html,
    'telegram': cmd_telegram,
}


def main(argv: list[str], stdin: TextIO, stdout: TextIO) -> int:
    parser = ArgumentParser()
    parser.add_argument('cmd', choices=sorted(COMMANDS))
    parser.add_argument('--pdb', action='store_true')
    parser.add_argument('--post')
    args: argparse.Namespace = parser.parse_args(argv)
    cmd = COMMANDS[args.cmd]
    try:
        return cmd(args)
    except Exception:
        if args.pdb:
            pdb.post_mortem()
        raise


def entrypoint() -> NoReturn:
    sys.exit(main(sys.argv[1:], sys.stdin, sys.stdout))
