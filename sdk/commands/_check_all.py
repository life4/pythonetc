from __future__ import annotations

from pathlib import Path

from ..post import Post
from ..sequence import PostSequence
from ._command import Command


class CheckAllCommand(Command):
    """Check all posts."""
    name = 'check-all'

    def run(self) -> int:
        known_post_paths: set[Path] = set()

        for path in Path('posts').iterdir():
            if path.suffix != '.md':
                continue
            post = Post.from_path(path)
            if post.id is not None and post.id <= 100:
                post.run_code()  # TODO: all posts should be runnable
            if post.sequence:
                assert post.path.absolute() in [
                    p.path.absolute() for p in post.sequence.posts
                ], f'{post.path.name} is not in its sequence'

            known_post_paths.add(path.absolute())

        # check sequences
        for path in Path('posts/sequences').iterdir():
            if path.suffix != '.yaml':
                continue
            sequence = PostSequence.from_path(path)
            for post_of_seq in sequence.posts:
                assert post_of_seq.path.absolute() in known_post_paths,\
                    f'unknown post {post_of_seq.path} in {path.name}'

        return 0
