from python_mermaid.diagram import MermaidDiagram
from .utils import *

def test_setup_diagram_with_only_a_title():
    m = MermaidDiagram(title=DUMMY_TITLE)
    assert str(m) == simple_diagram

def test_diagram_with_only_a_node():
    m = MermaidDiagram(title=DUMMY_TITLE, nodes=[NODE_1])
    print(diagram_with_one_node)
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

def test_adding_nodes_to_diagram():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1]
    )
    assert str(m) == diagram_with_one_node
    m.add_nodes([NODE_2])
    assert str(m) == diagram_with_multiple_nodes

def test_adding_links_to_diagram():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1, NODE_2],
        links=[LINK_1, LINK_2],
    )
    assert str(m) == diagram_with_nodes_and_links
    m.add_links([LINK_3])
    assert str(m) == (
        diagram_with_nodes_and_links + f"\n{str(LINK_3)}"
    )

def test_diagram_with_subgraph():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[BIG_NODE_1,NODE_2]
    )
    assert str(m) == diagram_with_subgraphs

def test_diagram_with_interactions():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1],
        interactions=[INTERACTION_1]
    )
    assert str(m) == diagram_with_interactions

def test_diagram_without_title():
    m = MermaidDiagram()
    assert str(m) == diagram_without_title
