from typing import List
from .node import Node
from .link import Link
from .interaction import Interaction

DIAGRAM_TYPES = {
    "default": "graph",
    "flowchart": "flowchart",
    "statechart": "stateDiagram-v2"
}

DIAGRAM_ORIENTATION = {
    "default": "",
    "top to bottom": "TB",
    "top-down": "TD",
    "bottom to top": "BT",
    "right to left": "RL",
    "left to right": "LR",
}


class MermaidDiagram:
    def __init__(
        self,
        title: str = "",
        nodes: List[Node] = [],
        links: List[Link] = [],
        interactions: List[Interaction] = [],
        type="default",
        orientation="default"
    ):
        self.title = title
        self.nodes = nodes
        self.links = links
        self.interactions = interactions
        self.type = DIAGRAM_TYPES[type]
        self.orientation = DIAGRAM_ORIENTATION[orientation]

    def add_nodes(self, nodes=[]):
        self.nodes += nodes

    def add_links(self, links=[]):
        self.links += links

    def __getGraphStr(self):
        nodes_string = (
            '\n'.join([str(node) for node in self.nodes])
        )
        links_string = (
            '\n'.join([str(link) for link in self.links])
        )
        interactions_string = (
            '\n'.join([str(interaction) for interaction in self.interactions])
        )
        final_strings = list(
            filter(
                None,
                [
                    f"{self.type} {self.orientation}",
                    nodes_string,
                    links_string,
                    interactions_string
                ]
            )
        )
        return '\n'.join(final_strings)
    
    def __getStateDiagramStr(self):
        nodes_string = (
            '\n'.join([str(node) for node in self.nodes if str(node)!=""])
        )
        links_string = (
            '\n'.join([str(link) for link in self.links])
        )
        final_strings = list(
            filter(
                None,
                [
                    f"{self.type}",
                    nodes_string,
                    links_string
                ]
            )
        )
        return '\n'.join(final_strings)

    def __str__(self):
        self.string = f"---\ntitle: {self.title}\n---\n" if self.title else ""
        content = ""
        if self.type == "graph":
            content = self.__getGraphStr()
        elif self.type == "stateDiagram-v2":
            content = self.__getStateDiagramStr()
        self.string += content
        return self.string
        
