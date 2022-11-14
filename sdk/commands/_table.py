
from __future__ import annotations

from ..post import get_posts
from ._command import Command


class TableCommand(Command):
    """Print ASCII table of posts.
    """
    name = 'table'

    def run(self) -> int:
        for post in sorted(get_posts().values()):
            self.print(
                post.published or 'TBA       ',
                f'PEP {post.pep:<4}' if post.pep else ' ' * 8,
                f'{post.python:<4}' if post.python else ' ' * 4,
                f'{post.path.name:26}',
                f'{post.title}',
                sep=' | ',
            )
        return 0
