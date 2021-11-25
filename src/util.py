import os
import re

TAG_RE = re.compile(r'\{[a-zA-Z0-9-]+\}')

def parse(file):
    dir, filename = os.path.split(file)
    base, ext = os.path.splitext(filename)
    raw_tags = TAG_RE.findall(base)
    tags = set()

    for raw_tag in raw_tags:
        base = base.replace(raw_tag, '')
        tags.add(raw_tag[1:-1])

    return {
        'base': base,
        'dir': dir,
        'ext': ext,
        'tags': tags,
    }

def unparse(file_obj):
    tags = sorted(file_obj['tags'])
    return file_obj['dir']\
        + '/'\
        + file_obj['base']\
        + '{' + '}{'.join(tags) + '}'\
        + file_obj['ext']
