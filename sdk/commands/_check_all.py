from __future__ import annotations

from pathlib import Path

from ..post import Post
from ..sequence import PostSequence
from ._command import Command


class CheckAllCommand(Command):
    """Check all posts."""
    name = 'check-all'

    def run(self) -> int:
        known_posts_by_path: dict[Path, Post] = {}
        known_post_ids: set[int] = set()

        for path in Path('posts').iterdir():
            if path.suffix != '.md':
                continue
            post = Post.from_path(path)
            if error := post.validate():
                raise ValueError(f'invalid {post.path.name}: {error}')
            if post.id is not None and post.id <= 100:
                try:
                    post.run_code()  # TODO: all posts should be runnable
                except BaseException as e:
                    raise ValueError(
                        f'Error occurred while running {post.path.name}: {e}'
                    ) from e
                assert '' != post.telegram_markdown
            if post.id:
                assert post.id not in known_post_ids, f'duplicate post id: {post.id}'
            if post.sequence:
                assert post.path.absolute() in [
                    p.path.absolute() for p in post.sequence.posts
                ], f'{post.path.name} is not in its sequence'

            known_posts_by_path[path.absolute()] = post
            if post.id is not None:
                known_post_ids.add(post.id)

        # check sequences
        for path in Path('posts/sequences').iterdir():
            if path.suffix != '.yaml':
                continue
            sequence = PostSequence.from_path(path)
            for post_of_seq in sequence.posts:
                assert post_of_seq.path.absolute() in known_posts_by_path,\
                    f'unknown post {post_of_seq.path} in {path.name}'
                post = known_posts_by_path[post_of_seq.path.absolute()]
                assert post.sequence == sequence

        return 0
