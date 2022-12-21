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
    def __init__(
        self,
        origin: Node,
        end: Node,
        shape: str = "arrow-head",
        message: str = ""
    ):
        self.origin = origin
        self.end = end
        self.shape = LINK_SHAPES[shape]
        self.message = message

    def __str__(self):
        s = ""
        if not self.message:
            s = f"{self.origin.id} {self.shape} {self.end.id}"
        else:
            s = f"{self.origin.id} {self.shape} |{self.message}| {self.end.id}"
        return s
