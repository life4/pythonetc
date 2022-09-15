
from __future__ import annotations
import argparse
from pathlib import Path

from ._command import Command
from ..post import Post


class TelegramCommand(Command):
    """Print Telegram-friendly Markdown for the given post.
    """
    name = 'telegram'

    @classmethod
    def init_parser(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('post', type=Path)

    def run(self) -> int:
        self.print(Post.from_path(self.args.post).telegram_markdown)
        return 0
