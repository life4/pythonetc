import io
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

    output = io.StringIO()
    output.write(dedent(f'''
    ---
    published: {date}
    id: {target_id}
    author: pushtaev
    ---

    # ...

    ''').lstrip())

    for line in target['text']:
        if isinstance(line, str):
            output.write(line)
        elif isinstance(line, dict):
            if line['type'] == 'bold':
                output.write('**{}**'.format(line['text']))
            elif line['type'] == 'italic':
                output.write('*{}*'.format(line['text']))
            elif line['type'] == 'code':
                output.write('`{}`'.format(line['text']))
            elif line['type'] == 'pre':
                output.write('```python\n')
                output.write(line['text'] + '\n')
                output.write('```\n')
            elif line['type'] == 'text_link':
                output.write('[{}]({})'.format(line['text'], line['href']))
            elif line['type'] in ('mention', 'link'):
                output.write('{}'.format(line['text']))
            else:
                raise ValueError('Unknown line type: {}'.format(line['type']))
        else:
            raise ValueError('Unknown line type: {}'.format(type(line)))

    output_string = output.getvalue()
    while "\n\n\n" in output_string:
        output_string = output_string.replace("\n\n\n", "\n\n")

    with open(f'posts/__{target_id}__.md', 'w', encoding='utf8') as f2:
        f2.write(output_string + "\n")


if __name__ == '__main__':
    main()
