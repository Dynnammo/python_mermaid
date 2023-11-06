import pytest
from .utils import NODE_1, NODE_2

def test_node():
    assert str(NODE_1) == ""

def test_node_with_name():
    assert str(NODE_2) == f"state \"{NODE_2.content}\" as {NODE_2.id}"
