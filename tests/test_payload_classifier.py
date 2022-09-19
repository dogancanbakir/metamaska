import pytest

from metamaska.payload_classifier import PayloadClassifier


@pytest.fixture
def payload_classifier():
    return PayloadClassifier()

def test_ctor():
    with pytest.raises(ValueError):
        PayloadClassifier("")

def test_valid(payload_classifier):
    assert payload_classifier.predict("meta") == "valid"

def test_empty(payload_classifier):
    with pytest.raises(ValueError):
        payload_classifier.predict("")


def test_sqli(payload_classifier):
    assert payload_classifier.predict("' OR 1 -- -") == "sqli"


def test_xss(payload_classifier):
    assert payload_classifier.predict("\"onfocus=\"alert('Y000')\"+autofocus=\"") == "xss"
