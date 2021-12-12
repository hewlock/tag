from .. import __version__
import click

@click.command('version')
def version_command():
    '''Show version information.

    \b
    Examples:
      - tag version
    '''
    show_version()

def show_version():
    click.echo(__version__)
