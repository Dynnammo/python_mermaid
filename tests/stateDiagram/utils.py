from python_mermaid.link import StateLink
from python_mermaid.node import StateNode

DUMMY_TITLE = "My diagram"
NODE_1 = StateNode(
    "test"
)
NODE_2 = StateNode(
    "My first node"
)

NODE_3 = StateNode(
    "My second node",
    "Different Title"
)

LINK_1 = StateLink(
    NODE_2,
    NODE_3
)

LINK_2 = StateLink(
    NODE_2,
    NODE_1
)

LINK_3 = StateLink(
    NODE_1,
    NODE_3,
    "Link comment"
)

def replace_all(string, dict):
    for k, v in dict.items():
        string = string.replace(k, v)
    return string

diagram_without_title = open('tests/stateDiagram/diagram_files/diagram_without_title', 'r').read()

simple_diagram = replace_all(
    open('tests/stateDiagram/diagram_files/simple_diagram', 'r').read(),
    {'DUMMY_TITLE': DUMMY_TITLE}
)

diagram_with_one_node = open('tests/stateDiagram/diagram_files/diagram_with_one_node', 'r').read()
diagram_with_multiple_nodes = open('tests/stateDiagram/diagram_files/diagram_with_multiple_nodes', 'r').read()
diagram_with_short_comment = open('tests/stateDiagram/diagram_files/diagram_with_short_comment', 'r').read()
diagram_with_long_comment = open('tests/stateDiagram/diagram_files/diagram_with_long_comment', 'r').read()
diagram_with_nodes_and_links = open('tests/stateDiagram/diagram_files/diagram_with_nodes_and_links', 'r').read()
diagram_with_start_end_node = open('tests/stateDiagram/diagram_files/diagram_with_start_end_nodes', 'r').read()
