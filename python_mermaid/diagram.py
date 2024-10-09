from typing import List, Optional
from .node import AbstractNode, Node
from .link import Link
from .interaction import Interaction

DIAGRAM_TYPES = {
    "default": "graph",
    "flowchart": "flowchart",
    "statechart": "stateDiagram-v2",
}

DIAGRAM_ORIENTATION = {
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
        nodes: Optional[List[Node]] = None,
        links: Optional[List[Link]] = None,
        interactions: Optional[List[Interaction]] = None,
        type="default",
        orientation="top-down",
    ):
        self.title = title
        self.type = DIAGRAM_TYPES[type]
        self.orientation = DIAGRAM_ORIENTATION[orientation]
        self.graph = Graph(
            header=f"{self.type} {self.orientation}",
            nodes=nodes,
            links=links,
            interactions=interactions,
        )

    def add_nodes(self, nodes=[]):
        self.graph.add_nodes(nodes)

    def add_links(self, links=[]):
        self.graph.add_links(links)

    def add_start_and_end_nodes(
        self,
        start_node: Optional[AbstractNode] = None,
        end_node: Optional[AbstractNode] = None,
    ):
        self.graph.add_start_and_end_nodes(start_node, end_node)

    def add_subgraph(self, name: str) -> "Graph":
        return self.graph.add_subgraph(name)

    def __str__(self) -> str:
        s = f"---\ntitle: {self.title}\n---\n" if self.title else ""
        content = ""
        if self.type == "graph":
            content = self.graph.get_graph_str()
        elif self.type == "stateDiagram-v2":
            content = self.graph.get_state_diagram_str()
        s += content
        return s


class Graph:
    def __init__(
        self,
        header: str,
        nodes: Optional[List[Node]] = None,
        links: Optional[List[Link]] = None,
        interactions: Optional[List[Interaction]] = None,
    ):
        self.header = header
        self.nodes = nodes if type(nodes) is list else []
        self.links = links if type(links) is list else []
        self.interactions = interactions if type(interactions) is list else []
        self.startNode = None
        self.endNode = None
        self.sub_graphs = []

    def add_nodes(self, nodes=[]):
        self.nodes += nodes

    def add_links(self, links=[]):
        self.links += links

    def add_start_and_end_nodes(
        self,
        start_node: Optional[AbstractNode] = None,
        end_node: Optional[AbstractNode] = None,
    ):
        self.startNode = start_node  # type: ignore
        self.endNode = end_node  # type: ignore

    def add_subgraph(self, name: str) -> "Graph":
        s = Graph(f"subgraph {name}")
        self.sub_graphs.append(s)
        return s

    def get_graph_str(self):
        nodes_string = "\n".join([str(node) for node in self.nodes])
        links_string = "\n".join([str(link) for link in self.links])
        interactions_string = "\n".join(
            [str(interaction) for interaction in self.interactions]
        )
        sub_graphs = "\n".join([f"{g.get_graph_str()}\nend" for g in self.sub_graphs])
        final_strings = list(
            filter(
                None,
                [
                    self.header,
                    nodes_string,
                    links_string,
                    interactions_string,
                    sub_graphs,
                ],
            )
        )
        return "\n".join(final_strings)

    def get_state_diagram_str(self):
        nodes_string = "\n".join([str(node) for node in self.nodes if str(node) != ""])
        links_string = "\n".join([str(link) for link in self.links])
        sub_graphs = "\n".join(
            [f"{g.get_state_diagram_str()}\nend" for g in self.sub_graphs]
        )
        final_strings = list(
            filter(
                None,
                [
                    f"{self.header}",
                    nodes_string,
                    f"[*] --> {self.startNode.id}" if self.startNode else None,
                    links_string,
                    f"{self.endNode.id} --> [*]" if self.endNode else None,
                    sub_graphs,
                ],
            )
        )
        return "\n".join(final_strings)
