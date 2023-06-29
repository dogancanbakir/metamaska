import click

from metamaska.metamaska import Metamaska


@click.command(no_args_is_help=True)
@click.option('-m', '--meta', required=True, help = "meta string to evaluate")
@click.option('-p', '--proba', default=False, help = "probability of given meta")
def main(meta, proba):
    if not meta:
        raise ValueError("meta string is required.")

    print(Metamaska().form(meta, proba))


if __name__ == "__main__":
    main()  # pragma: no cover
