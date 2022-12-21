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
    def __init__(self, id: str, content: str = None, shape: str = "normal"):
        self.id = id
        self.content = content if content else id
        self.shape = NODE_SHAPES[shape]

        # TODO: verify that content match a working string pattern

    def __str__(self):
        return f"{self.id}{self.shape.start}\"{self.content}\"{self.shape.end}"
