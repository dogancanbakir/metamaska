import pytest

from metamaska.metamaska import Metamaska


@pytest.fixture
def metamaska():
    return Metamaska()


def test_valid(metamaska):
    assert metamaska.form("meta") == "valid"

def test_empty(metamaska):
    with pytest.raises(ValueError):
        metamaska.form("")


def test_sqli(metamaska):
    assert metamaska.form("' OR 1 -- -") == "sqli"


def test_xss(metamaska):
    assert metamaska.form("\"onfocus=\"alert('Y000')\"+autofocus=\"") == "xss"
