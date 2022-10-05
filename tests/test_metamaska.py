import pytest

from metamaska.metamaska import Metamaska


@pytest.fixture
def metamaska():
    return Metamaska()


def test_form_with_valid_case(metamaska):
    assert metamaska.form("meta") == "valid"


def test_form_with_valid_case(metamaska):
    cls, proba = metamaska.form("meta", True)

    assert cls == "valid"
    assert proba >= 0.99


def test_form_with_empty_str(metamaska):
    with pytest.raises(ValueError):
        metamaska.form("")


def test_form_with_sqli_case(metamaska):
    assert metamaska.form("' OR 1 -- -") == "sqli"


def test_form_with_xss_case(metamaska):
    assert metamaska.form("\"onfocus=\"alert('Y000')\"+autofocus=\"") == "xss"
