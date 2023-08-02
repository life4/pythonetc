
from __future__ import annotations

import asyncio
import os
import re
from functools import cached_property
from pathlib import Path

from telethon import TelegramClient

from ..post import Post
from ._command import Command


CHANNEL = 'pythonetc'
REX_URL = re.compile(r'https?\:[a-zA-Z0-9\-\/\.\(]+')
REX_PYTHON = re.compile(r'3\.[0-9]{1,2}')
REX_QNAME = re.compile(r'[a-z]{2,}\.[a-zA-Z0-9]{2,}')
URLs = tuple[str, ...]


class AddIDsCommand(Command):
    """Add Telegram post IDs to all posts that don't have it.
    """
    name = 'add-ids'

    def run(self) -> int:
        if 'API_ID' not in os.environ:
            self.warn(
                'API_ID and API_HASH env vars required, '
                'you can get them at https://my.telegram.org/apps',
            )
            return 1
        asyncio.run(self._run())
        return 0

    async def _run(self) -> None:
        self.print('reading posts...')
        paths = self._get_paths()
        self.print('fetching IDs...')
        async with self._client:
            ids = await self._get_ids()
        self.print('setting IDs...')
        for keyword, id in ids.items():
            path = paths.get(keyword)
            if path is None:
                continue
            content = path.read_text(encoding='utf-8')
            lines = content.splitlines()
            lines.insert(2, f'id: {id}')
            new_content = '\n'.join(lines)
            new_content = new_content.rstrip() + '\n'
            assert new_content != content
            path.write_text(new_content, encoding='utf-8')
            self.print(f'added ID for {path.name}')

    def _get_paths(self) -> dict[URLs, Path]:
        paths: dict[URLs, Path] = {}
        for path in sorted(Path('posts').iterdir()):
            if path.suffix != '.md':
                continue
            post = Post.from_path(path)
            if post.id is not None:
                continue
            keywords = self._get_keywords(post.md_content)
            if not keywords:
                continue
            if keywords in paths:
                name1 = path.name
                name2 = paths[keywords].name
                msg = f'duplicate set of keywords: {name1} and {name2}'
                raise RuntimeError(msg)
            paths[keywords] = path
        return paths

    async def _get_ids(self) -> dict[URLs, int]:
        ids = {}
        async for message in self._client.iter_messages(CHANNEL):
            if message.text is None:
                continue
            keywords = self._get_keywords(message.text)
            if not keywords:
                continue
            if keywords in ids:
                continue
            ids[keywords] = message.id
        return ids

    def _get_keywords(self, text: str) -> URLs:
        """
        Get some key components from the text (URLs, qualnames, Python versions)
        that can be used to uniquely identify a text.

        It allows us to match the same text ignoring changes in formatting
        or corrected typos.
        """
        result = REX_URL.findall(text)
        result.extend(REX_PYTHON.findall(text))
        result.extend(REX_QNAME.findall(text))
        return tuple(result)

    @cached_property
    def _client(self) -> TelegramClient:
        return TelegramClient(
            'bot',
            api_id=os.environ['API_ID'],
            api_hash=os.environ['API_HASH'],
        )
