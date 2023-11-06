import pytest
from python_mermaid.link import Link
from .utils import LINK_1, LINK_2

def test_link_without_message():
    assert str(LINK_1) == f"{LINK_1.origin.id} --> {LINK_1.end.id}"

def test_link_with_message():
    assert str(LINK_2) == f"{LINK_2.origin.id} --> {LINK_2.end.id}: {LINK_2.message}"
