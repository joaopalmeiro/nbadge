import click


# https://click.palletsprojects.com/en/8.1.x/setuptools/
@click.command()
def main():
    """Generate Jupyter notebook badges for different services."""
    click.echo("Hello World!")
