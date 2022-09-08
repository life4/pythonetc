from __future__ import annotations
from argparse import ArgumentParser
from datetime import date
from pathlib import Path
import sys
from typing import Callable, Mapping, NoReturn, TextIO
from .post import Post

try:
    import ipdb as pdb
except ImportError:
    import pdb  # type: ignore

Command = Callable[[], int]
ROOT = Path(__file__).parent.parent


def get_posts() -> list[Post]:
    posts: list[Post] = []
    posts_path = ROOT / 'posts'
    for path in posts_path.iterdir():
        if path.suffix != '.md':
            continue
        posts.append(Post.from_path(path))
    posts.sort(key=lambda post: post.published or date.today())
    return posts


def cmd_table() -> int:
    for post in get_posts():
        pep = f'PEP {post.pep:<4}' if post.pep else ' ' * 8
        python = f'{post.python:<4}' if post.python else ' ' * 4
        print(f'{post.published} | {pep} | {python} | {post.title}')
    return 0


COMMANDS: Mapping[str, Command] = {
    'table': cmd_table,
}


def main(argv: list[str], stdin: TextIO, stdout: TextIO) -> int:
    parser = ArgumentParser()
    parser.add_argument('cmd', choices=sorted(COMMANDS))
    parser.add_argument('--pdb', action='store_true')
    args = parser.parse_args(argv)
    cmd = COMMANDS[args.cmd]
    try:
        return cmd()
    except Exception:
        if args.pdb:
            pdb.post_mortem()
        raise


def entrypoint() -> NoReturn:
    sys.exit(main(sys.argv[1:], sys.stdin, sys.stdout))
