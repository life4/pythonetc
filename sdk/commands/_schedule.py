
from __future__ import annotations

import argparse
import asyncio
import os
from datetime import date, datetime, time, timedelta
from functools import cached_property
from pathlib import Path
from zoneinfo import ZoneInfo

from telethon import TelegramClient
from telethon.types import Message

from ..post import Post
from ._command import Command


CHANNEL = 'pythonetc'
TZ = ZoneInfo('Europe/Amsterdam')


class ScheduleCommand(Command):
    """Add post in scheduled messages in the Telegram channel.
    """
    name = 'schedule'

    @classmethod
    def init_parser(cls, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('post', type=Path)

    def run(self) -> int:
        post = Post.from_path(self.args.post)
        assert not post.sequence
        assert not post.markdown.has_images()
        assert not post.buttons

        if 'API_ID' not in os.environ:
            self.warn(
                'API_ID and API_HASH env vars required, '
                'you can get them at https://my.telegram.org/apps',
            )
            return 1

        error = asyncio.run(self._schedule(post))
        if error:
            self.warn(error)
            return 1
        return 0

    async def _schedule(self, post: Post) -> str | None:
        # check if the publish date is known and in the future
        if not post.published:
            return 'post must have `published` set'
        if post.published < date.today():
            return 'post already published'

        async with self._client:
            scheduled = await self._get_scheduled()
            if post.published in scheduled:
                return 'post already scheduled'

            # schedule the post
            publish_at = datetime.combine(post.published, time(16, 0, tzinfo=TZ))
            in10m = datetime.now(TZ) + timedelta(minutes=10)
            if publish_at < in10m:
                publish_at = in10m
            await self._client.send_message(
                CHANNEL,
                post.telegram_markdown,
                schedule=publish_at,
                link_preview=False,
            )
            self.print(f'post is scheduled to be published at {post.published}')
            return None

    async def _get_scheduled(self) -> list[date]:
        result = []
        message: Message
        async for message in self._client.iter_messages(CHANNEL, scheduled=True):
            assert message.date
            result.append(message.date.date())
        return result

    @cached_property
    def _client(self) -> TelegramClient:
        return TelegramClient(
            'bot',
            api_id=os.environ['API_ID'],
            api_hash=os.environ['API_HASH'],
        )
