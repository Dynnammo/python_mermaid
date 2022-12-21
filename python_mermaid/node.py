from .utils import snake_case
from typing import List


class NodeShape:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end

# Shapes are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#node-shapes


NODE_SHAPES = {
    "normal": NodeShape("[", "]"),
    "round-edge": NodeShape("(", ")"),
    "stadium-shape": NodeShape("([", "])"),
    "subroutine-shape": NodeShape("[[", "]]"),
    "cylindrical": NodeShape("[(", ")]"),
    "circle": NodeShape("((", "))"),
    "label-shape": NodeShape(">", "]"),
    "rhombus": NodeShape("{", ")"),
    "hexagon": NodeShape("{{", ")}"),
    "parallelogram": NodeShape("[/", "/]"),
    "parallelogram-alt": NodeShape("[\\", "\\]"),
    "trapezoid": NodeShape("[/", "\\]"),
    "trapezoid-alt": NodeShape("[\\", "/]"),
    "double-circle": NodeShape("(((", ")))"),
}


class Node:
    def __init__(
        self,
        id: str,
        content: str = None,
        shape: str = "normal",
        sub_nodes: List['Node'] = []
    ):
        self.id = snake_case(id)
        self.content = content if content else id
        self.shape = NODE_SHAPES[shape]
        self.sub_nodes = sub_nodes

        # TODO: verify that content match a working string pattern

    def add_sub_nodes(self, nodes: List['Node'] = []):
        self.sub_nodes += nodes

    def __str__(self):
        if len(self.sub_nodes):
            s = '\n'.join([
                f'subgraph {self.id} ["{self.content}"]',
                '\n'.join([str(node) for node in self.sub_nodes]),
                "end"
            ])
        else:
            s = ''.join([
                self.id,
                self.shape.start,
                '"' + self.content + '"',
                self.shape.end
            ])
        return s
