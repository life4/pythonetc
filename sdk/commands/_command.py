from __future__ import annotations

import argparse
import sys
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

    def print(self, *args, sep='\n') -> None:
        print(*args, file=self.stdout, sep=sep)

    def warn(self, message: str) -> None:
        sys.stderr.write(f'WARNING: {message}\n')
