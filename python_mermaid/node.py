# Shapes are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#node-shapes
NODE_SHAPES = {
    "normal": {"start":"[","end":"]"},
    "round-edge": {"start":"(","end":")"},
    "stadium-shape": {"start":"([","end":"])"},
    "subroutine-shape": {"start":"[[","end":"]]"},
    "cylindrical": {"start":"[(","end":")]"},
    "circle": {"start":"((","end":"))"},
    "label-shape": {"start":">","end":"]"},
    "rhombus": {"start":"{","end":"}"},
    "hexagon": {"start":"{{","end":"}}"},
    "parallelogram": {"start":"[/","end":"/]"},
    "parallelogram-alt": {"start":"[\\","end":"\\]"},
    "trapezoid": {"start":"[/","end":"\\]"},
    "trapezoid-alt": {"start":"[\\","end":"/]"},
    "double-circle": {"start":"(((","end":")))"},
}

class Node:
    def __init__(self, id: str, content: str = None, shape: str = "normal"):
        self.id = id
        self.content = content if content else id
        self.shape = NODE_SHAPES[shape]

        # TODO: verify that content match a working string pattern

    def __str__(self):
        return f"{self.id}{self.shape['start']}\"{self.content}\"{self.shape['end']}"
