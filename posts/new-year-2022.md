---
published: 2021-12-31
id: 685
author: orsinium
---

# new year 2021-2022

channel = '@pythonetc'
print(f'Happy new Year, {channel}!')

`#` there are our top posts from 2021
by_likes = {
    '[join-lists](https://t.me/pythonetc/652)': 236,
    '[dev-mode](https://t.me/pythonetc/676)': 181,
    '[is-warning](https://t.me/pythonetc/653)': 170,
    '[str-concat](https://t.me/pythonetc/650)': 166,
    '[class-scope](https://t.me/pythonetc/646)': 149,
}
by_forwards = {
    '[class-scope](https://t.me/pythonetc/646)': 111,
    '[dev-mode](https://t.me/pythonetc/676)': 53,
    '[join-lists](https://t.me/pythonetc/652)': 50,
    '[str-concat](https://t.me/pythonetc/650)': 44,
    '[eval-strategy](https://t.me/pythonetc/658)': 36,
}
by_views = {
    '[__path__](https://t.me/pythonetc/674)': 7_736,
    '[dev-mode](https://t.me/pythonetc/676)': 7_113,
    '[immutable](https://t.me/pythonetc/666)': 6_757,
    '[class-scope](https://t.me/pythonetc/646)': 6_739,
    '[sre-parse](https://t.me/pythonetc/678)': 6_661,
}

from datetime import date
from textwrap import dedent
if date.today().year == 2022:
  print(dedent("""
    The season 2.6 is coming!
    This is what awaits:
  """))
  print(
    'native telegram reactions instead of buttons',
    'deep dive into garbage collection, generators, and coroutines',
    'the season is still ran by @orsinium',
    'as always, guest posts and donations are welcome',
    sep='\n',
  )

print('See you next year \N{Sparkling Heart}!')
