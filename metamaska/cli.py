import click

from metamaska.metamaska import Metamaska


@click.command()
@click.option('--meta')
def main(meta, help="malevolent payload"):
    if not meta:
        raise ValueError("meta is required.")

    mm = Metamaska()
    click.echo(mm.form(meta))


if __name__ == "__main__":
    main()  # pragma: no cover
