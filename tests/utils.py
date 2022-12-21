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

diagram_simple = (
f"""---
title: {DUMMY_TITLE}
---
graph """
)

diagram_with_one_node = (
f"""---
title: {DUMMY_TITLE}
---
graph 
{NODE_1.id}["{NODE_1.content}"]"""
)

diagram_with_multiple_nodes = (
    diagram_with_one_node + f"""\n{NODE_2.id}["{NODE_2.content}"]"""
)

diagram_with_nodes_and_links = (
    diagram_with_multiple_nodes +
    f"""\n{LINK_1.origin.id} {LINK_1.head_left}{LINK_1.shape}{LINK_1.head_right} {LINK_1.end.id}""" +
    f"""\n{LINK_2.origin.id} {LINK_2.head_left}{LINK_2.shape}{LINK_2.head_right} {LINK_2.end.id}"""
)

diagram_with_subgraphs = (
f"""---
title: {DUMMY_TITLE}
---
graph 
subgraph my_big_node ["My big node"]
{str(NODE_1)}
end
{str(NODE_2)}"""
)

diagram_with_interactions = (
f"""---
title: {DUMMY_TITLE}
---
graph 
{str(NODE_1)}
{str(INTERACTION_1)}"""
)