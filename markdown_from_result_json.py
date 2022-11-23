import json
import sys
from pathlib import Path
from textwrap import dedent


def main():
    meta = json.loads(Path('result.json').read_text('utf8'))
    target_id = int(sys.argv[1])

    filtered = [x for x in meta['messages'] if x['id'] == target_id]
    assert len(filtered) == 1, (
        'Found not exactly one message (but {}) with id {}'.format(
            len(filtered), target_id
        )
    )
    target = filtered[0]
    date = target['date'][0:10]

    with open(f'posts/__{target_id}__.md', 'w', encoding='utf8') as f:
        f.write(dedent(f'''
        ---
        published: {date}
        id: {target_id}
        author: pushtaev
        ---

        # ...

        ''').lstrip())

        for line in target['text']:
            if isinstance(line, str):
                f.write(line)
            elif isinstance(line, dict):
                if line['type'] == 'bold':
                    f.write('*{}*'.format(line['text']))
                elif line['type'] == 'italic':
                    f.write('_{}_'.format(line['text']))
                elif line['type'] == 'code':
                    f.write('`{}`'.format(line['text']))
                elif line['type'] == 'pre':
                    f.write('```python\n')
                    f.write(line['text'] + '\n')
                    f.write('```\n')
                elif line['type'] == 'text_link':
                    f.write('[{}]({})'.format(line['text'], line['href']))
                elif line['type'] == 'mention':
                    f.write('{}'.format(line['text']))
                else:
                    raise ValueError('Unknown line type: {}'.format(line['type']))
            else:
                raise ValueError('Unknown line type: {}'.format(type(line)))


if __name__ == '__main__':
    main()
