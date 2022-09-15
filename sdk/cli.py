from __future__ import annotations

from argparse import ArgumentParser
import sys
from typing import NoReturn, TextIO
from .commands import Command, COMMANDS


try:
    import ipdb as pdb
except ImportError:
    import pdb  # type: ignore


def main(argv: list[str], stdout: TextIO) -> int:
    parser = ArgumentParser()
    parser.add_argument('--pdb', action='store_true')
    subparsers = parser.add_subparsers()
    parser.set_defaults(cmd=None)
    cmd_class: type[Command]
    for cmd_class in COMMANDS:
        subparser = subparsers.add_parser(
            name=cmd_class.name,
            help=cmd_class.__doc__,
        )
        subparser.set_defaults(cmd=cmd_class)
        cmd_class.init_parser(subparser)

    args = parser.parse_args(argv)
    cmd_class = args.cmd
    if cmd_class is None:
        parser.print_help()
        return 1
    cmd = cmd_class(args=args, stdout=stdout)
    try:
        return cmd.run()
    except Exception:
        if args.pdb:
            pdb.post_mortem()
        raise


def entrypoint() -> NoReturn:
    sys.exit(main(sys.argv[1:], sys.stdout))
