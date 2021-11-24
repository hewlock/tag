import click

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--verbose/--quiet', default=False)
def cli(ctx, verbose):
    '''tag-cli: filename tags v0.1'''
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose

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
      tag add mytag myfile.txt
      tag add mytag1,mytag2 *.txt
    '''
    print(f'tags: {tags}')
    print(f'files: {files}')
    


add.__doc__ = 'hi'
