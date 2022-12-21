import pytest
from python_mermaid.node import Node
from .utils import NODE_1, NODE_2

def test_node():
    assert str(NODE_1) == f"{NODE_1.id}{NODE_1.shape['start']}\"{NODE_1.content}\"{NODE_1.shape['end']}"
