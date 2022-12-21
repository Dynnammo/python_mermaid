from .node import Node

# Link are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#links-between-nodes
LINK_SHAPES = {
    "normal": "---",
    "dotted": "-.-",
    "thick": "==="
}

LINK_HEADS = {
    "none": "",
    "arrow": ">",
    "left-arrow": "<",
    "bullet": "o",
    "cross": "x"
}


class Link:
    def __init__(
        self,
        origin: Node,
        end: Node,
        shape: str = "normal",
        head_left: str = "none",
        head_right: str = "arrow",
        message: str = ""
    ):
        self.origin = origin
        self.end = end
        self.head_left = LINK_HEADS[head_left]
        self.head_right = LINK_HEADS[head_right]
        self.shape = LINK_SHAPES[shape]
        self.message = message

    def __str__(self):
        elements = [
            self.origin.id + " ",
            self.head_left,
            self.shape,
            self.head_right,
            f"|{self.message}|" if self.message else "",
            " " + self.end.id
        ]
        return "".join(elements)
