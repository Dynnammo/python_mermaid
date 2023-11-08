import pytest
from python_mermaid.node import AbstractNode
from .utils import NODE_1, NODE_2

def test_node():
    assert str(NODE_1) == f"{NODE_1.id}{NODE_1.shape.start}\"{NODE_1.content}\"{NODE_1.shape.end}"

def test_add_sub_nodes():
    n1 = NODE_1
    n2 =  NODE_2
    assert len(n1.sub_nodes) == 0
    assert len(n2.sub_nodes) == 0
    
    n1.add_sub_nodes([n2])
    assert len(n1.sub_nodes) == 1
    assert len(n2.sub_nodes) == 0
    assert n1.sub_nodes[0] == n2
