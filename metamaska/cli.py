import click

from metamaska.metamaska import Metamaska


@click.command(no_args_is_help=True)
@click.option('-m', '--meta', required=True, help = "meta to find form for")
@click.option('-p', '--proba', default=False, help = "To compute probability of given meta")
def main(meta, proba):
    if not meta:
        raise ValueError("meta is required.")

    print(Metamaska().form(meta, proba))


if __name__ == "__main__":
    main()  # pragma: no cover
