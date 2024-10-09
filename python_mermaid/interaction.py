from typing import List
from .node import Node

# List of all interactions are documented here
# https://mermaid.js.org/syntax/flowchart.html#interaction
INTERACTION_TYPE = {"link": "href", "callback": "call callback()"}


class Interaction:
    def __init__(self, node: Node, type: str = "link", args: List[str] = []):
        self.node = node
        self.type = INTERACTION_TYPE[type]
        self.args = args if args else None

    def __str__(self):
        return f"click {self.node.id} {self.type} {' '.join(self.args)}"
