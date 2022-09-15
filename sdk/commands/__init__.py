
from ._command import Command
from ._html import HTMLCommand
from ._table import TableCommand
from ._telegram import TelegramCommand

__all__ = ['Command', 'COMMANDS']

COMMANDS = (HTMLCommand, TableCommand, TelegramCommand)
