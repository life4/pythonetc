from __future__ import annotations

import io
import re
import sys
from dataclasses import dataclass
from functools import cached_property
from typing import Iterable, Optional


@dataclass
class IPythonCommand:
    in_: str
    out: str
    real_out: Optional[str] = None


class IPythonCommandBuffer:
    def __init__(self):
        self._in_buffer: str = ''
        self._out_buffer: str = ''

        self._out_started = False

    def add_in(self, s: str) -> None:
        if self._in_buffer and self._in_buffer[-1] == '\\':
            self._in_buffer = self._in_buffer[:-1] + s
        elif self._in_buffer:
            self._in_buffer += '\n' + s
        else:
            self._in_buffer = s

    def add_out(self, s: str) -> None:
        self._out_started = True
        self._out_buffer += s

    def add_unknown(self, s: str) -> None:
        if self._out_started:
            self.add_out(s)
        else:
            self.add_in(s)

    def is_empty(self) -> bool:
        return not self._in_buffer and not self._out_buffer

    def reset(self) -> IPythonCommand:
        result = IPythonCommand(
            in_=self._in_buffer,
            out=self._out_buffer,
            real_out=None,
        )
        self._in_buffer = ''
        self._out_buffer = ''
        self._out_started = False

        return result


class IPythonExecutor:
    def __init__(self, code: str) -> None:
        self._code = code

    @cached_property
    def _commands(self) -> list[IPythonCommand]:
        result = []

        buffer = IPythonCommandBuffer()
        for line in self._code.splitlines():
            if m := re.fullmatch(r'In ?(?:\[\d+])?: (.*)', line):
                if not buffer.is_empty():
                    result.append(buffer.reset())
                buffer.add_in(m.group(1))
            elif m := re.fullmatch(r'Out(?:\[\d+])?: (.*)', line):
                buffer.add_out(m.group(1))
            elif m := re.fullmatch(r'\s*[.]{3}:(?: (.*))?', line):
                if m.group(1) is not None:
                    buffer.add_unknown(m.group(1))
            else:
                pass  # unexpected line, probably output

        if not buffer.is_empty():
            result.append(buffer.reset())

        return result

    def run(self, shared_globals: dict) -> Iterable[IPythonCommand]:
        orig_stdin = sys.stdin
        orig_stdout = sys.stdout
        real_out: dict[int, str] = {}
        try:
            sys.stdin = io.StringIO('\n\n'.join(c.in_ for c in self._commands) + '\n')
            sys.stdout = io.StringIO()

            from IPython import embed
            shared_globals['embed'] = embed
            shared_globals['__name__'] = __name__
            exec('embed()', shared_globals)

            out_lines = sys.stdout.getvalue().splitlines()
            if any(('-' * 40) in line for line in out_lines):
                raise RuntimeError(
                    'Looks like exception in IPython occurred.\n'
                    + 'Now follows the whole original output:\n'
                    + '\n'.join(f"OUTPUT WITH ERROR: {line}" for line in out_lines)
                )

            for out_line in out_lines:
                if m := re.search(r'Out\[(\d+)]: (.*)$', out_line):
                    real_out[int(m.group(1))] = m.group(2)
        finally:
            if orig_stdin is not None:
                sys.stdin = orig_stdin
            if orig_stdout is not None:
                sys.stdout = orig_stdout

        cnt = 1
        for cmd in self._commands:
            yield IPythonCommand(
                in_=cmd.in_,
                out=cmd.out,
                real_out=real_out.get(int(cnt), ''),
            )
            cnt += 1
