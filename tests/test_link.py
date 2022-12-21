import pytest
from python_mermaid.link import Link
from .utils import LINK_1, LINK_2

def test_link_without_message():
    assert str(LINK_1) == f"{LINK_1.origin.id} {LINK_1.shape} {LINK_1.end.id}"

def test_link_with_message():
    l = LINK_1
    l.message = "This is a message"
    assert str(l) == f"{l.origin.id} {l.shape} |{l.message}| {l.end.id}"
