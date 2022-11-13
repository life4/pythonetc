from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Iterable


if TYPE_CHECKING:
    from .post import Post
    from .trace import Trace


@dataclass
class Module:
    name: str = ''
    root_post: Post | None = None
    child_posts: list[tuple[Trace, Post]] = field(default_factory=list)

    @classmethod
    def from_posts(self, posts: Iterable[Post]) -> list[Module]:
        modules: defaultdict[str, Module] = defaultdict(Module)
        for post in posts:
            for trace in post.traces:
                name = trace.module_name
                if not name or name == 'builtins':
                    continue
                modules[name].name = name
                if trace.is_module:
                    modules[name].root_post = post
                else:
                    modules[name].child_posts.append((trace, post))
        return sorted(modules.values(), key=lambda m: m.name)
