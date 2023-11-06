import pytest
from .utils import NODE_1, NODE_2, NODE_3

def test_node():
    assert str(NODE_1) == ""
    assert repr(NODE_1) == f"{NODE_1.id}['{NODE_1.content}']"

def test_node_with_name():
    assert str(NODE_2) == f"state \"{NODE_2.content}\" as {NODE_2.id}"

def test_node_with_different_name():
    assert str(NODE_3) == f"state \"{NODE_3.content}\" as {NODE_3.id}"