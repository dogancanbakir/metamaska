import pytest

from metamaska.utils import unquote, remove_new_line, remove_whitespace


def test_unquote():
    assert unquote("\"onfocus=\"alert('Y000')\"+autofocus=\"") == "\"onfocus=\"alert('Y000')\" autofocus=\""


def test_remove_new_line():
    assert remove_new_line("payload\n") == "payload"


def test_remove_whitespace():
    assert remove_whitespace(" payload ") == "payload"
