import click
import os
import re

TAG_RE = re.compile(r'\{[a-zA-Z0-9-]+\}')

def get_raw_tags(filename):
    return TAG_RE.findall(filename)

def get_tag(raw_tag):
    return raw_tag[1:-1]

def get_tags(filename):
    return map(get_tag, get_raw_tags(filename))

def parse(file):
    dir, filename = os.path.split(file)
    base, ext = os.path.splitext(filename)
    raw_tags = get_raw_tags(base)
    tags = set()

    for raw_tag in raw_tags:
        base = base.replace(raw_tag, '')
        tags.add(get_tag(raw_tag))

    return {
        'base': base,
        'dir': dir,
        'ext': ext,
        'tags': tags,
    }

def unparse(file_obj):
    tags = sorted(file_obj['tags'])
    tag_text = '{' + '}{'.join(tags) + '}' if len(tags) > 0 else ''
    return file_obj['dir']\
        + '/'\
        + file_obj['base']\
        + tag_text\
        + file_obj['ext']

def rename_files(verbose, debug, files, tag_handler):
    count = 0
    for src in files:
        file_obj = parse(src)
        tag_handler(file_obj['tags'])
        dst = unparse(file_obj)
        if src == dst:
            continue
        if verbose:
            click.echo(f"{src} -> {dst}")
        if not debug:
            os.rename(src, dst)
            count += 1
    if verbose and count > 0:
        click.echo()
        click.echo(f"{count} files affected.")
