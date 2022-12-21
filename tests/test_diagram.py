import pytest
from python_mermaid.diagram import MermaidDiagram, Node, Link
from .utils import *  # noqa

def test_setup_diagram_with_only_a_title():
    m = MermaidDiagram(title=DUMMY_TITLE)
    assert str(m) == diagram_simple

def test_diagram_with_only_a_node():
    m = MermaidDiagram(title=DUMMY_TITLE, nodes=[NODE_1])
    assert str(m) == diagram_with_one_node

def test_diagram_with_multiple_nodes():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1, NODE_2]
    )
    assert str(m) == diagram_with_multiple_nodes
    
def test_diagram_with_nodes_and_links():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1, NODE_2],
        links=[LINK_1, LINK_2]
    )
    assert str(m) == diagram_with_nodes_and_links
