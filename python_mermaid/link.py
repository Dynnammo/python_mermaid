from .node import AbstractNode, StateNode
from .utils import sanitize_string

# Link are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#links-between-nodes
LINK_SHAPES = {"normal": "---", "dotted": "-.-", "thick": "==="}

LINK_HEADS = {"none": "", "arrow": ">", "left-arrow": "<", "bullet": "o", "cross": "x"}


class Link:
    def __init__(
        self,
        origin: AbstractNode,
        end: AbstractNode,
        shape: str = "normal",
        head_left: str = "none",
        head_right: str = "arrow",
        message: str = "",
    ):
        self.origin = origin
        self.end = end
        self.head_left = LINK_HEADS[head_left]
        self.head_right = LINK_HEADS[head_right]
        self.shape = LINK_SHAPES[shape]
        self.message = sanitize_string(message)

    def __str__(self):
        elements = [
            self.origin.id + " ",
            self.head_left,
            self.shape,
            self.head_right,
            f"|{self.message}|" if self.message else "",
            " " + self.end.id,
        ]
        return "".join(elements)


class StateLink(Link):
    def __init__(self, origin: StateNode, end: StateNode, message: str = ""):
        super().__init__(origin, end, "normal", "none", "arrow", message)

    def __str__(self):
        element = f"{self.origin.id} --> {self.end.id}"
        if self.message != "":
            element += f": {self.message}"
        return element
