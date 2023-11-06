import pytest
from python_mermaid.link import Link
from .utils import LINK_1, LINK_3

def test_link_without_message():
    assert str(LINK_1) == f"{LINK_1.origin.id} --> {LINK_1.end.id}"

def test_link_with_message():
    assert str(LINK_3) == f"{LINK_3.origin.id} --> {LINK_3.end.id}: {LINK_3.message}"
