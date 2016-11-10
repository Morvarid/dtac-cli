import click


@click.command()
@click.argument('action_type')
@click.argument('sub_action')
@click.option('--item', '-o', nargs=2)
@click.option('--username', prompt='Your username')
@click.option('--password', hide_input=True, prompt='Your password')
def main(action_type, sub_action, username, password, item):
    """This package provides a command line interface to DTAC"""

    if sub_action == 'cp':
        click.echo('Coping files from this path {0} to {1} ...'.format(item[0], item[1]))
