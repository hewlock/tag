import click
import os
import src.util as util

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--verbose', '-v', default=False, is_flag=True, help='Print additional output.')
@click.option('--debug', '-d', default=False, is_flag=True, help='Make no changes to the file system.')
def cli(ctx, verbose, debug):
    '''tag-cli: filename tags v0.1

    \b
    File tags:
      - are in the file name directly before the extension
      - start with '{' and end with '}'
      - consist of letters, numbers and the '-' character

    \b
    Examples:
      - myfile{my-tag-1}{my-tag-2}.txt
      - My Title Case File {My-Tag-1}{My-Tag-2}.txt
    '''
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose
    ctx.obj['debug'] = debug

@cli.command()
@click.pass_context
@click.argument('tags')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def add(ctx, tags, files):
    '''Add tags to files.

    \b
    TAGS  comma seperated list of tags
    FILES list of files

    \b
    Examples:
      - tag add my-tag myfile.txt
      - tag add my-tag-1,my-tag-2 *.txt
    '''
    add_tags = tags.split(',')
    for src in files:
        file_obj = util.parse(src)
        file_obj['tags'].update(add_tags)
        dst = util.unparse(file_obj)
        if ctx.obj['verbose']:
            print(f"{src} -> {dst}")
        if not ctx.obj['debug']:
            os.rename(src, dst)
