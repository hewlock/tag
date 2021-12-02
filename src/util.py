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
        'filename': filename,
        'original': file,
        'tags': tags,
    }

def unparse(file_obj):
    tags = sorted(file_obj['tags'])
    tag_text = '{' + '}{'.join(tags) + '}' if len(tags) > 0 else ''
    return os.path.join(file_obj['dir'], f"{file_obj['base']}{tag_text}{file_obj['ext']}")

def rename_files(verbose, debug, files, tag_handler):
    count = 0
    for src in files:
        count += 1
        file_obj = parse(src)
        tag_handler(file_obj['tags'])
        dst = unparse(file_obj)
        if src == dst:
            continue
        if verbose:
            click.echo(f"{src} -> {dst}")
        if not debug:
            os.rename(src, dst)
    if verbose and count > 0:
        message = 'to rename' if debug else 'renamed'
        click.echo()
        click.echo(f"{count} files {message}.")

def find_files(path, recursive, all, handler):
    def filename_p(filename):
        return all or not filename.startswith('.')

    def found(root, file):
        handler(parse(os.path.join(root, file)))

    if recursive:
        for root, dirs, files in os.walk(path):
            for file in filter(filename_p, files):
                found(root, file)
    else:
        for entry in os.scandir(path):
            if entry.is_file() and filename_p(entry.name):
                found(path, entry.name)

def permute(items, tree):
    if tree:
        return _permute([], items)
    return map(lambda item: [item], items)

def _permute(prefix, suffix):
    result = [prefix] if prefix else []
    if not suffix:
        return result
    for index, item in enumerate(suffix):
        child_prefix = prefix.copy()
        child_prefix.append(item)
        child_suffix = suffix.copy()
        del child_suffix[index]
        result = result + _permute(child_prefix, child_suffix)
    return result

def tree_output(path, files):
    head, tail = os.path.split(path)
    root = {
        'children': [],
        'dir': True,
        'name': path,
        'path': head if tail == '' else path,
    }

    index = 0;
    node = root
    done = False
    while not done:
        head, tail = os.path.split(files[index])
        if head == node['path']:
            node['children'].append({
                'dir': False,
                'name': tail,
            })
            index += 1
            done = index == len(files)
            continue

        if head.startswith(node['path']):
            new_path = None
            while head != node['path']:
                new_path = head
                head, tail = os.path.split(head)
            node = {
                'children': [],
                'dir': True,
                'name': tail,
                'path': new_path,
                'parent': node,
            }
            node['parent']['children'].append(node)
        else:
            node = node['parent']

    return node_output(root, '', [root['name']])

def node_output(node, prefix, output):
    children = node['children']
    for index, child in enumerate(children):
        child_prefix = None
        if (index + 1 == len(children)):
            child_prefix = f'{prefix}    '
            output.append(f"{prefix}└── {child['name']}")
        else:
            child_prefix = f'{prefix}│   '
            output.append(f"{prefix}├── {child['name']}")

        if child['dir']:
            node_output(child, child_prefix, output)
    return output
