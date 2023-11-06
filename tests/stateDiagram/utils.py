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
    NODE_1,
    NODE_2
)
LINK_2 = StateLink(
    NODE_1,
    NODE_2,
    "Example message"
)
