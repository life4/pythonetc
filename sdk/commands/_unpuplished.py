
from __future__ import annotations

from ..post import get_posts
from ._command import Command


class UnpublishedCommand(Command):
    """List posts that don't have publish time set yet.
    """
    name = 'unpublished'

    def run(self) -> int:
        for post in get_posts():
            if post.published is None:
                self.print(f'{post.path.name:20} {post.title}')
        return 0
