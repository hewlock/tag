from . import arguments
from . import options
from . import util
from .commands.add import add_command
from .commands.clear import clear_command
from .commands.find import find_command
from .commands.index import index_command
from .commands.list import list_command
from .commands.remove import remove_command
from .commands.rename import rename_command
from .commands.set import set_command
from .commands.sort import sort_command
from .commands.version import version_command, show_version
import click

@click.group(invoke_without_command=True)
@options.version()
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
        show_version()
    elif ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

cli.add_command(add_command)
cli.add_command(clear_command)
cli.add_command(find_command)
cli.add_command(index_command)
cli.add_command(list_command)
cli.add_command(remove_command)
cli.add_command(rename_command)
cli.add_command(set_command)
cli.add_command(sort_command)
cli.add_command(version_command)
