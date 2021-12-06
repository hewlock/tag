from .. import arguments
from .. import options
from .. import util
import click

@click.command('find')
@options.all()
@options.null()
@options.recursive()
@options.tree()
@arguments.tag()
@arguments.path()
def find_command(all, null, recursive, tree, tag, path):
    '''Find files by tag.

    \b
    TAG  tag to find
    PATH path to search (default .)

    \b
    Examples:
      - tag find -r my-tag path/to/files/
      - tag find my-tag
    '''
    file_list = []
    def handle_file(file):
        if tag in file['tags']:
            file_list.append(file)
    util.find_files(path, recursive, all, handle_file)

    file_list = sorted(map(lambda f: f['original'], file_list))
    output = util.tree_output(path, file_list) if tree else file_list
    delimiter = '\0' if null else '\n'
    click.echo(delimiter.join(output), nl = not null)
