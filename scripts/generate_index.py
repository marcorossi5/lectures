#!/usr/bin/env python3
"""Generate slides/index.html from templates/index_template.html."""

import os
import re
from datetime import datetime

SLIDES_DIR = 'slides'
TEMPLATE_PATH = 'templates/index_template.html'
PATTERN = re.compile(r'^(\d{8})_(.+)$')


def main():
    entries = []
    for name in sorted(os.listdir(SLIDES_DIR), reverse=True):
        m = PATTERN.match(name)
        if m and os.path.isdir(os.path.join(SLIDES_DIR, name)):
            date_str, slug = m.group(1), m.group(2)
            date = datetime.strptime(date_str, '%Y%m%d')
            title = ' '.join(w[0].upper() + w[1:] for w in slug.split('_'))
            entries.append((date, name, title))

    cards = '\n'.join(
        '<a class="card" href="./' + name + '/">\n'
        '  <span class="date">' + date.strftime('%d %b %Y') + '</span>\n'
        '  <span class="title">' + title + '</span>\n'
        '</a>'
        for date, name, title in entries
    )

    with open(TEMPLATE_PATH) as f:
        template = f.read()

    output_path = os.path.join(SLIDES_DIR, 'index.html')
    with open(output_path, 'w') as f:
        f.write(template.replace('CARDS_PLACEHOLDER', cards))

    print(f'Generated {output_path} with {len(entries)} lecture(s).')


if __name__ == '__main__':
    main()
