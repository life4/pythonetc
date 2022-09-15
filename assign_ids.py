from pathlib import Path
import json


meta = json.loads(Path('result.json').read_text('utf8'))
dates = {}
for msg in meta['messages']:
    if msg['type'] == 'message':
        d = msg['date'].split('T')[0]
        dates[d] = msg['id']

for pp in Path('posts').iterdir():
    if pp.is_dir():
        continue
    t = pp.read_text('utf8')
    for d, id in dates.items():
        t = t.replace(f'published: {d}', f'published: {d}\nid: {id}')
    pp.write_text(t, 'utf8')
