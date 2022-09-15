from __future__ import annotations
import argparse
from dataclasses import dataclass
from typing import ClassVar, TextIO


@dataclass
class Command:
    name: ClassVar[str]
    args: argparse.Namespace
    stdout: TextIO

    @classmethod
    def init_parser(cls, parser: argparse.ArgumentParser) -> None:
        pass

    def run(self) -> int:
        raise NotImplementedError

    def print(self, *args) -> None:
        print(*args, file=self.stdout)
