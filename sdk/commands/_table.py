
from __future__ import annotations

from ..post import get_posts
from ._command import Command


class TableCommand(Command):
    """Print ASCII table of posts.
    """
    name = 'table'

    def run(self) -> int:
        for post in get_posts():
            pep = f'PEP {post.pep:<4}' if post.pep else ' ' * 8
            python = f'{post.python:<4}' if post.python else ' ' * 4
            self.print(f'{post.published} | {pep} | {python} | {post.title}')
        return 0
