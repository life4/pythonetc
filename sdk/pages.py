from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Page:
    title: str
    url: str
    descr: str


PAGES: tuple[Page, ...] = (
    Page(
        'python versions', 'pythons.html',
        'Posts grouped by the Python version they cover.',
    ),
    Page(
        'peps', 'peps.html',
        'Posts describing specific PEPs',
    ),
    Page(
        'stdlib', 'stdlib.html',
        'Posts covering specific modules or function in stdlib.',
    ),
    Page(
        'typing', 'typing.html',
        'Posts about type annotations.',
    ),
)
