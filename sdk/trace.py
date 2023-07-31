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
        k, v = next(iter(raw.items()))
        return cls(k, v)


@dataclass
class Trace:
    crumbs: list[Crumb]

    @classmethod
    def from_raw(cls, raw: list[dict]) -> Trace:
        return Trace([Crumb.from_raw(crumb) for crumb in raw])

    @cached_property
    def types(self) -> list[str]:
        return [c.type for c in self.crumbs]

    @property
    def is_module(self) -> bool:
        return self.types == ['module']

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

    @cached_property
    def title(self) -> str:
        result = ''
        for crumb in self.crumbs:
            if crumb.type not in ('keyword', 'arg'):
                if result:
                    result += '.'
                result += crumb.name
            if crumb.type == 'decorator':
                result = f'@{result}'
            if crumb.type == 'arg':
                result += f'({crumb.name})'
        return result

    @cached_property
    def docs_url(self) -> str | None:
        """Link to the page in oficial Python docs.
        """
        if self.is_module:
            return f'https://docs.python.org/3/library/{self.module_name}.html'
        if len(self.crumbs) == 2 and self.crumbs[0].type == 'module':
            mod = self.crumbs[0].name
            obj = self.crumbs[1].name
            return f'https://docs.python.org/3/library/{mod}.html#{mod}.{obj}'
        return None
