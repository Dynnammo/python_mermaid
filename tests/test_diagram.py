import pytest
from python_mermaid.mermaid import MermaidDiagram, Node, Link

DUMMY_TITLE = "My diagram"
DUMMY_NODE = Node(
    "My first node"
)
DUMMY_NODE_2 = Node(
    "My second node"
)
LINK_1 = Link(
    DUMMY_NODE,
    DUMMY_NODE_2
)
LINK_2 = Link(
    DUMMY_NODE_2,
    DUMMY_NODE
)

diagram_simple = (
f"""---
title: {DUMMY_TITLE}
---
graph 

"""
)

diagram_with_one_node = (
f"""---
title: {DUMMY_TITLE}
---
graph 
{DUMMY_NODE.id}["{DUMMY_NODE.content}"]
"""
)

diagram_with_multiple_nodes = (
    diagram_with_one_node + f"""{DUMMY_NODE_2.id}["{DUMMY_NODE_2.content}"]\n"""
)

diagram_with_nodes_and_links = (
    diagram_with_multiple_nodes + 
    f"""{LINK_1.origin.id} {LINK_1.shape} {LINK_1.end.id}\n""" +
    f"""{LINK_2.origin.id} {LINK_2.shape} {LINK_2.end.id}"""
)

def test_setup_diagram_with_only_a_title():
    m = MermaidDiagram(title=DUMMY_TITLE)
    assert str(m) == diagram_simple

def test_diagram_with_only_a_node():
    m = MermaidDiagram(title=DUMMY_TITLE, nodes=[DUMMY_NODE])
    assert str(m) == diagram_with_one_node

def test_diagram_with_multiple_nodes():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[DUMMY_NODE, DUMMY_NODE_2]
    )
    assert str(m) == diagram_with_multiple_nodes
    
def test_diagram_with_nodes_and_links():
    m = MermaidDiagram(
        title=DUMMY_TITLE,
        nodes=[DUMMY_NODE, DUMMY_NODE_2],
        links=[LINK_1, LINK_2]
    )
    assert str(m) == diagram_with_nodes_and_links
