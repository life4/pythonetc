It was a long break but tomorrow we start again. We have plenty of ideas for posts but don't always have time to write them. So, this is how you can help us:

+ If you have something to tell about Python (syntax, stdlib, PEPs), check if it already was posted. If not, write a post, send it to us, and we will publish it. It will include your name (if you want to), we don't steal content ;)

+ If you don't have an idea, just contact us, we have plenty of them! And if you like it, the algorithm is the same as above: write a post, send it, we publish it with your name.

+ If you don't have time to write posts but still want to help, consider donating a bot of money. If we get enough, we can take a one-day vacation and invest it exclusively into writing posts.

+ If you see a bug or typo in a post, please, let us know!

And speaking about bugs, there are few in recent posts that our lovely subscribers have reported:

+ [post #641](https://t.me/pythonetc/641), reported by @recursing. `functools.cache` isn't faster than `functools.lru_cache(maxsize=None)`, it is exactly the same. The confusion comes from [the documentation](https://docs.python.org/3/library/functools.html#functools.cache) which says "this is smaller and faster than lru_cache() WITH A SIZE LIMIT".

+ [post #644](https://t.me/pythonetc/644), reported by @el71Gato. It should be `10**8` instead of `10*8`. We re-run benchmarks with these values, relative numbers are the same, so all conclusions are still correct.

Welcome into season 2.5 :)
