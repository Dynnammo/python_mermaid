import pytest
from python_mermaid.link import Link
from .utils import LINK_1, LINK_2

def test_link_without_message():
    l = LINK_1
    assert str(LINK_1) == f"{l.origin.id} {l.head_left}{LINK_1.shape}{l.head_right} {LINK_1.end.id}"

def test_link_with_message():
    l = LINK_1
    l.message = "This is a message"
    assert str(l) == f"{l.origin.id} {l.head_left}{l.shape}{l.head_right}|{l.message}| {l.end.id}"
