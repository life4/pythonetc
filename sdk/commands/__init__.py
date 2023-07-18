from ._check_all import CheckAllCommand
from ._command import Command
from ._html import HTMLCommand
from ._run_code import RunCodeCommand
from ._schedule import ScheduleCommand
from ._table import TableCommand
from ._telegram import TelegramCommand


__all__ = ['Command', 'COMMANDS']

COMMANDS = (
    HTMLCommand,
    RunCodeCommand,
    ScheduleCommand,
    TableCommand,
    TelegramCommand,
    CheckAllCommand,
)
