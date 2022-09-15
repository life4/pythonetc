from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Page:
    title: str
    url: str
    descr: str


PAGES: tuple[Page, ...] = (
    Page(
        'telegram', 'https://t.me/s/pythonetc',
        'all posts we make are created for the Telegram channel first.'
    ),
    Page(
        'all posts', 'posts.html',
        'All posts we ever published, sorted by date.',
    ),
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
)
