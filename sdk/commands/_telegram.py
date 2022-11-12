
from __future__ import annotations

import argparse
from pathlib import Path

from ..post import Post
from ._command import Command


class TelegramCommand(Command):
    """Print Telegram-friendly Markdown for the given post.
    """
    name = 'telegram'

    @classmethod
    def init_parser(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('post', type=Path)

    def run(self) -> int:
        post = Post.from_path(self.args.post)
        self.print(post.telegram_markdown)

        if post.sequence:
            index = post.self_in_sequence().index
            if len(post.sequence.posts) > index + 1:
                next_post = post.sequence.posts[index + 1]
                if not next_post.delay_allowed:
                    self.warn(
                        f'Next post must be posted immediately: '
                        f'python -m sdk telegram posts/{next_post.path.name}'
                    )


        return 0
