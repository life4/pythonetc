from __future__ import annotations

from pathlib import Path
from typing import TypeVar, Type

import attr
import yaml

PostSequenceT = TypeVar('PostSequenceT', bound='PostSequence')


@attr.s(auto_attribs=True, frozen=True)
class PostOfSequence:
    path: Path
    delay_allowed: bool = False


@attr.s(auto_attribs=True, frozen=True)
class PostSequence:
    posts: list[PostOfSequence]

    @classmethod
    def from_path(cls: Type[PostSequenceT], path: Path) -> PostSequenceT:
        data: dict = yaml.safe_load(path.read_text('utf8'))

        posts: list[PostOfSequence] = []
        for post in data['posts']:
            if 'name' in post:
                assert 'path' not in post,\
                    f'path and name are mutually exclusive in {path.name}'
                post['path'] = Path('posts') / (post.pop('name') + '.md')
            if 'post' in post:
                post['path'] = Path(post['path'])

            posts.append(PostOfSequence(**post))

        return cls(posts=posts)
