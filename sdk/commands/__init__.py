
from ._command import Command
from ._html import HTMLCommand
from ._run_code import RunCodeCommand
from ._table import TableCommand
from ._telegram import TelegramCommand
from ._unpuplished import UnpublishedCommand


__all__ = ['Command', 'COMMANDS']

COMMANDS = (
    HTMLCommand,
    RunCodeCommand,
    TableCommand,
    TelegramCommand,
    UnpublishedCommand,
)
