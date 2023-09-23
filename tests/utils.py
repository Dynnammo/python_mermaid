from python_mermaid.link import Link
from python_mermaid.node import Node
from python_mermaid.interaction import Interaction
from python_mermaid.diagram import (
    MermaidDiagram
)

DUMMY_TITLE = "My diagram"
NODE_1 = Node(
    "My first node"
)
NODE_2 = Node(
    "My second node"
)
INTERACTION_1 = Interaction(
    NODE_1,
    args=["https://wikipedia.org"]
)
BIG_NODE_1 = Node(
    "My big node",
    sub_nodes=[NODE_1]
)
LINK_1 = Link(
    NODE_1,
    NODE_2
)
LINK_2 = Link(
    NODE_2,
    NODE_1
)
LINK_3 = Link(
    NODE_1,
    NODE_2,
    shape="thick"
)

def replace_all(string, dict):
    for k, v in dict.items():
        string = string.replace(k, v)
    return string

simple_diagram = replace_all(
    open('tests/diagram_files/simple_diagram','r').read(),
    {'DUMMY_TITLE':DUMMY_TITLE}
)

diagram_with_one_node = replace_all(
    open('tests/diagram_files/diagram_with_one_node','r').read(),
    {
        'DUMMY_TITLE':DUMMY_TITLE,
        'NODE_1.id': NODE_1.id,
        'NODE_1.content': NODE_1.content
    }
)

diagram_with_multiple_nodes = (
    diagram_with_one_node + f"""\n{NODE_2.id}["{NODE_2.content}"]"""
)

diagram_with_nodes_and_links = (
    diagram_with_multiple_nodes +
    f"""\n{LINK_1.origin.id} {LINK_1.head_left}{LINK_1.shape}{LINK_1.head_right} {LINK_1.end.id}""" +
    f"""\n{LINK_2.origin.id} {LINK_2.head_left}{LINK_2.shape}{LINK_2.head_right} {LINK_2.end.id}"""
)

diagram_with_subgraphs = replace_all(
    open('tests/diagram_files/diagram_with_subgraphs','r').read(),
    {
        'DUMMY_TITLE':DUMMY_TITLE,
        'NODE_2.id': NODE_2.id,
        'NODE_2.content': NODE_2.content,
        'NODE_1.id': NODE_1.id,
        'NODE_1.content': NODE_1.content
    }
)

diagram_with_interactions = replace_all(
    open('tests/diagram_files/diagram_with_interactions','r').read(),
    {
        'DUMMY_TITLE':DUMMY_TITLE,
        'NODE_1.id': NODE_1.id,
        'NODE_1.content': NODE_1.content,
        'INTERACTION_1.type': INTERACTION_1.type,
        'INTERACTION_1.args': INTERACTION_1.args[0]
    }
)
