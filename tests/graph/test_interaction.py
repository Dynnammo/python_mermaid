from python_mermaid.interaction import Interaction
from python_mermaid.node import AbstractNode
from .utils import *

def test_interaction():
    i = INTERACTION_1
    assert str(i) == f"click {i.node.id} {i.type} {' '.join(i.args)}"
