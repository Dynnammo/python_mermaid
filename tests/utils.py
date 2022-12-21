from python_mermaid.link import Link
from python_mermaid.node import Node
from python_mermaid.mermaid import (
    MermaidDiagram,
    FlowChartDiagramm
)

DUMMY_TITLE = "My diagram"
NODE_1 = Node(
    "My first node"
)
NODE_2 = Node(
    "My second node"
)
LINK_1 = Link(
    NODE_1,
    NODE_2
)
LINK_2 = Link(
    NODE_2,
    NODE_1
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
{NODE_1.id}["{NODE_1.content}"]
"""
)

diagram_with_multiple_nodes = (
    diagram_with_one_node + f"""{NODE_2.id}["{NODE_2.content}"]\n"""
)

diagram_with_nodes_and_links = (
    diagram_with_multiple_nodes + 
    f"""{LINK_1.origin.id} {LINK_1.shape} {LINK_1.end.id}\n""" +
    f"""{LINK_2.origin.id} {LINK_2.shape} {LINK_2.end.id}"""
)