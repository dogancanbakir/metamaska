from click.testing import CliRunner
from metamaska import cli


def test_cli():
    runner = CliRunner()
    result = runner.invoke(cli.main, ["-m", "<script>"])
    assert result.output == "xss\n"
