from __future__ import annotations

from pathlib import Path
from typing import Type, TypeVar

import attr
import yaml


PostSequenceT = TypeVar('PostSequenceT', bound='PostSequence')


@attr.s(auto_attribs=True, frozen=True)
class PostOfSequence:
    index: int
    path: Path
    delay_allowed: bool = False


@attr.s(auto_attribs=True, frozen=True)
class PostSequence:
    posts: list[PostOfSequence]

    @classmethod
    def from_path(cls: Type[PostSequenceT], path: Path) -> PostSequenceT:
        data: dict = yaml.safe_load(path.read_text('utf8'))

        posts: list[PostOfSequence] = []
        index = 0
        for post in data['posts']:
            if 'name' in post:
                msg = f'path and name are mutually exclusive in {path.name}'
                assert 'path' not in post, msg
                post['path'] = (Path('posts') / (post.pop('name') + '.md'))
            if 'post' in post:
                post['path'] = Path(post['path'])

            posts.append(PostOfSequence(index=index, **post))
            index += 1

        return cls(posts=posts)
