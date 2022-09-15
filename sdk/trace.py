from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property


def parse_traces(raw_traces: list[list[dict]]) -> list[Trace]:
    return [Trace.from_raw(trace) for trace in raw_traces]


@dataclass
class Crumb:
    type: str
    name: str

    @classmethod
    def from_raw(cls, raw: dict) -> Crumb:
        assert len(raw) == 1
        k, v = list(raw.items())[0]
        return cls(k, v)


@dataclass
class Trace:
    crumbs: list[Crumb]

    @classmethod
    def from_raw(cls, raw: list[dict]) -> Trace:
        return Trace([Crumb.from_raw(crumb) for crumb in raw])

    @cached_property
    def is_module(self) -> bool:
        if len(self.crumbs) != 1:
            return False
        return self.crumbs[0].type == 'module'

    @cached_property
    def module_name(self) -> str:
        """
        Module name where the object is defined.
        If the object is a module, returns the module name itself.
        """
        first_crumb = self.crumbs[0]
        if first_crumb.type == 'module':
            return first_crumb.name
        if first_crumb.type == 'keyword':
            return ''
        return 'builtins'
