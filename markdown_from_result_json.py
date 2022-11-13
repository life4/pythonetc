import json
import sys
from pathlib import Path

meta = json.loads(Path('result.json').read_text('utf8'))
target_id = int(sys.argv[1])

filtered = [x for x in meta['messages'] if x['id'] == target_id]
assert len(filtered) == 1, (
    "Found not exactly one message (but {}) with id {}".format(len(filtered), target_id)
)
target = filtered[0]

for line in target['text']:
    if isinstance(line, str):
        print(line, end='')
    elif isinstance(line, dict):
        if line['type'] == 'bold':
            print("*{}*".format(line['text']), end='')
        elif line['type'] == 'italic':
            print("_{}_".format(line['text']), end='')
        elif line['type'] == 'code':
            print("`{}`".format(line['text']), end='')
        elif line['type'] == 'pre':
            print("```python")
            print(line['text'])
            print("```")
        else:
            raise ValueError("Unknown line type: {}".format(line['type']))
    else:
        raise ValueError("Unknown line type: {}".format(type(line)))