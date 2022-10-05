import click

from metamaska.metamaska import Metamaska


@click.command()
@click.option('-m', '--meta', required=True, help="malevolent payload")
def main(meta):
    if not meta:
        raise ValueError("meta is required.")

    print(Metamaska().form(meta))


if __name__ == "__main__":
    main()  # pragma: no cover
