import click


# https://click.palletsprojects.com/en/8.1.x/setuptools/
@click.command()
# https://click.palletsprojects.com/en/8.1.x/quickstart/#adding-parameters
# https://click.palletsprojects.com/en/8.1.x/arguments/
@click.argument("url")
def main(url: str) -> None:
    """Generate Jupyter notebook badges for different services."""
    click.echo(url)
