
from __future__ import annotations

import argparse
from pathlib import Path

from ..post import Post, PostChain
from ._command import Command


class CheckAllCommand(Command):
    """Check all posts."""
    name = 'check_all'

    def run(self) -> int:
        all_chains: dict[str, dict[int, PostChain]] = {}

        for path in Path('posts').iterdir():
            if path.suffix != '.md':
                continue
            post = Post.from_path(path)
            # post.run_code()  # TODO: all posts should be runnable
            if post.chain:
                chain = all_chains.setdefault(post.chain.name, {})
                chain[post.id] = post.chain

        # check chains
        for chain_name, chains in all_chains.items():
            i = 0
            prev: int | None = None
            for post_id, chain in sorted(chains.items(), key=lambda p: p[1].idx):
                assert chain.idx == i
                assert chain.name == chain_name
                assert chain.length == len(chains)
                assert chain.prev is None or chain.prev in chains
                assert chain.prev is None or chains[chain.prev].next == post_id
                assert chain.prev == prev
                assert chain.next is None or chain.next in chains

                prev = post_id
                i += 1

        return 0
