import click
import os
import src.util as util

VERSION = '0.1'

# Options

def opt_debug():
    return click.option('--debug', '-d', default=False, is_flag=True, help='Make no changes to the file system.')

def opt_verbose():
    return click.option('--verbose', '-v', default=False, is_flag=True, help='Print additional output.')

def opt_version():
    return click.option('--version', default=False, is_flag=True, help='Print version.')

# Arguments

def arg_files():
    return click.argument('files', nargs=-1, type=click.Path(exists=True))

def arg_tags():
    return click.argument('tags')

def arg_old_tag():
    return click.argument('old_tag')

def arg_new_tag():
    return click.argument('new_tag')

# CLI

@click.group(invoke_without_command=True)
@opt_version()
@click.pass_context
def cli(ctx, version):
    '''tag-cli: file name tag manager

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
    if version:
        click.echo(VERSION)
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

@cli.command()
@opt_verbose()
@opt_debug()
@arg_tags()
@arg_files()
def add(verbose, debug, tags, files):
    '''Add tags to files.

    \b
    TAGS  comma seperated list of tags
    FILES list of files

    \b
    Examples:
      - tag add my-tag myfile.txt
      - tag add my-tag-1,my-tag-2 *.txt
    '''
    tag_list = tags.split(',')
    util.rename_files(verbose, debug, files, lambda tag_set: tag_set.update(tag_list))

@cli.command()
@opt_verbose()
@opt_debug()
@arg_files()
def clear(verbose, debug, files):
    '''Clear tags from files.

    \b
    FILES list of files

    \b
    Examples:
      - tag clear myfile{my-tag}.txt
      - tag clear *.txt
    '''
    util.rename_files(verbose, debug, files, lambda tag_set: tag_set.clear())

@cli.command()
@opt_verbose()
@opt_debug()
@arg_tags()
@arg_files()
def remove(verbose, debug, tags, files):
    '''Remove tags from files.

    \b
    TAGS  comma seperated list of tags
    FILES list of files

    \b
    Examples:
      - tag remove my-tag myfile{my-tag}.txt
      - tag remove my-tag-1,my-tag-2 *.txt
    '''
    tag_list = tags.split(',')
    util.rename_files(verbose, debug, files, lambda tag_set: tag_set.difference_update(tag_list))

@cli.command()
@opt_verbose()
@opt_debug()
@arg_old_tag()
@arg_new_tag()
@arg_files()
def rename(verbose, debug, old_tag, new_tag, files):
    '''Rename a tag on files.

    \b
    OLD_TAG current tag name
    NEW_TAG new tag name
    FILES list of files

    \b
    Examples:
      - tag rename my-tag my-new-tag myfile{my-tag}.txt
      - tag rename my-tag my-new-tag *.txt
    '''
    def tag_handler(tag_set):
        if old_tag in tag_set:
            tag_set.remove(old_tag)
            tag_set.add(new_tag)
    util.rename_files(verbose, debug, files, tag_handler)

@cli.command()
@opt_verbose()
@opt_debug()
@arg_tags()
@arg_files()
def set(verbose, debug, tags, files):
    '''Set tags on files.

    Add and remove tags to ensure each file has the supplied tags and only the supplied tags.

    \b
    TAGS  comma seperated list of tags
    FILES list of files

    \b
    Examples:
      - tag set my-tag myfile{my-tag}.txt
      - tag set my-tag-1,my-tag-2 *.txt
    '''
    tag_list = tags.split(',')
    def tag_handler(tag_set):
        tag_set.clear()
        tag_set.update(tag_list)
    util.rename_files(verbose, debug, files, tag_handler)

@cli.command()
@opt_verbose()
@opt_debug()
@arg_files()
def sort(verbose, debug, files):
    '''Sort tags on files.

    \b
    FILES list of files

    \b
    Examples:
      - tag sort myfile{my-tag-2}{my-tag-1}.txt
      - tag sort *.txt
    '''
    util.rename_files(verbose, debug, files, lambda tag_set: tag_set)
