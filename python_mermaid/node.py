from typing import List
from .utils import snake_case, sanitize_string


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
    "rhombus": NodeShape("{", "}"),
    "hexagon": NodeShape("{{", "}}"),
    "parallelogram": NodeShape("[/", "/]"),
    "parallelogram-alt": NodeShape("[\\", "\\]"),
    "trapezoid": NodeShape("[/", "\\]"),
    "trapezoid-alt": NodeShape("[\\", "/]"),
    "double-circle": NodeShape("(((", ")))"),
}


class AbstractNode:
    def __init__(self, id: str, content: str = ""):
        self.id = snake_case(id)
        self.content = content if content else id
        self.content = sanitize_string(self.content)

    def __repr__(self):
        return f"{self.id}['{self.content}']"


class Node(AbstractNode):
    def __init__(
        self,
        id: str,
        content: str = "",
        shape: str = "normal",
        sub_nodes: List = [],
    ):
        super().__init__(id, content)
        self.shape = NODE_SHAPES[shape]
        self.sub_nodes = sub_nodes

        # TODO: verify that content match a working string pattern

    def add_sub_nodes(self, new_nodes: List["Node"] = []):
        self.sub_nodes = self.sub_nodes + new_nodes

    def __repr__(self):
        return f"{self.id}['{self.content}'] Nb_children:{len(self.sub_nodes)}"

    def __str__(self):
        s = ""
        if len(self.sub_nodes):
            s += "\n".join(
                [
                    f'subgraph {self.id} ["{self.content}"]',
                    "\n".join([str(node) for node in self.sub_nodes]),
                    "end",
                ]
            )
        else:
            s += "".join(
                [self.id, self.shape.start, '"' + self.content + '"', self.shape.end]
            )
        return s


class StateNode(AbstractNode):
    def __init__(self, id: str, content: str = ""):
        self.id = snake_case(id)
        self.content = id if content == "" else content
        self.note = None

    def add_note(self, message, position="right"):
        self.note = {"message": message, "position": position}

    def __str__(self):
        if self.content == self.id:
            result = ""
        else:
            result = f'state "{self.content}" as {self.id}'
        if self.note:
            if "\n" in self.note["message"]:
                result += (
                    f"\nnote {self.note['position']} of {self.id}"
                    + f"\n{self.note['message']}"
                    + "\nend note"
                )
            else:
                result += (
                    f"\nnote {self.note['position']} of {self.id}: "
                    + f"{self.note['message']}"
                )
        return result
