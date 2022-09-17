from __future__ import annotations
import argparse
from pathlib import Path

from ._command import Command
from ..post import Post


class RunCodeCommand(Command):
    """Run code from the given post.
    """
    name = 'run-code'

    @classmethod
    def init_parser(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('post', type=Path)

    def run(self) -> int:
        Post.from_path(self.args.post).run_code()
        return 0
