import pytest

from metamaska.payload_classifier import PayloadClassifier


@pytest.fixture
def payload_classifier():
    return PayloadClassifier()


def test_ctor():
    with pytest.raises(ValueError):
        PayloadClassifier("")


def test_predict_with_valid_case(payload_classifier):
    assert payload_classifier.predict("meta") == "valid"


def test_predict_proba_with_valid_case(payload_classifier):
    y_pred_prob = payload_classifier.predict_proba("meta")
    index = y_pred_prob.argmax(1).item()

    assert payload_classifier.classes_[index] == "valid"
    assert y_pred_prob[0, index] >= 0.99


def test_predict_with_empty_str(payload_classifier):
    with pytest.raises(ValueError):
        payload_classifier.predict("")


def test_predict_with_sqli_case(payload_classifier):
    assert payload_classifier.predict("' OR 1 -- -") == "sqli"


def test_predict_with_xss_case(payload_classifier):
    assert payload_classifier.predict("\"onfocus=\"alert('Y000')\"+autofocus=\"") == "xss"
