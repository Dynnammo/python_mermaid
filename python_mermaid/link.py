from .node import Node

# Link are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#links-between-nodes
LINK_SHAPES = {
    "arrow-head": "-->",
    "open-link": "---",
    "dotted-link": "-.->",
    "thick-link": "==>"
}

class Link:
    def __init__(self, origin: Node, end: Node, shape: str = "arrow-head", message: str = ""):
        pass
    
    def __str__(self):
        if not message:
            return f"{origin.id} {LINK_SHAPES[self.shape]} {end.id}"
        else:
            return f"{origin.id} {LINK_SHAPES[self.shape]} |{message}| {end.id}"