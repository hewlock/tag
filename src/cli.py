import click
import os
import src.util as util

VERSION = '0.1'

@click.group(invoke_without_command=True)
@click.option('--version', default=False, is_flag=True, help='Print version.')
def cli(version):
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
        print(VERSION)

@cli.command()
@click.option('--verbose', '-v', default=False, is_flag=True, help='Print additional output.')
@click.option('--debug', '-d', default=False, is_flag=True, help='Make no changes to the file system.')
@click.argument('tags')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
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
    add_tags = tags.split(',')
    util.process_files(verbose, debug, files, lambda tag_set: tag_set.update(add_tags))

@cli.command()
@click.option('--verbose', '-v', default=False, is_flag=True, help='Print additional output.')
@click.option('--debug', '-d', default=False, is_flag=True, help='Make no changes to the file system.')
@click.argument('tags')
@click.argument('files', nargs=-1, type=click.Path(exists=True))
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
    remove_tags = tags.split(',')
    util.process_files(verbose, debug, files, lambda tag_set: tag_set.difference_update(remove_tags))
