CHART_TYPES = [
    "flowchart"
]

CHART_ORIENTATION = {
    "top to bottom": "TB",
    "top-down": "TD", 
    "bottom to top": "BT",
    "right to left": "RL",
    "left to right": "LR",
}

# Shapes are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#node-shapes
NODE_SHAPES = {
    "normal":{"start":"[","end":"]"},
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

# Link are created following the documentation here :
# https://mermaid.js.org/syntax/flowchart.html#links-between-nodes
LINK_SHAPES = {
    "arrow-head": "-->",
    "open-link": "---",
    "dotted-link": "-.->",
    "thick-link": "==>"
}
    


class MermaidDiagram:
    def __init__(self, title="", nodes=[], links=[]):
        self.title = title
        self.nodes = nodes
        self.links = links
    
    def add_nodes(self, nodes=[]):
        pass
        
    def add_links(self, links=[]):
        pass


class FlowChartDiagramm(MermaidDiagram):
    def __init__(self, title=None, orientation="top-down"):
        super().__init__(title)
        self.type = 'flowchart'
        self.orientation = CHART_ORIENTATION[orientation]


class Node:
    def __init__(self, id, content=None, shape="normal"):
        self.id = id
        self.content = content
        self.shape = shape
        
        if shape not in NODE_SHAPES.keys():
            raise ValueError(f"Shape given is not a normalized shape: {shape}. Please try one of the following: {str(NODE_SHAPES.keys())")
        
        # TODO : test id if matching a pattern

    def __str__(self):
        if content:
            return f"{id}{shape['start']}\"{content}\"{shape['end']}"
        else:
            return f"{id}{shape['start']}\"{content}\"{shape['end']}"


class Link:
    def __init__(self, origin, end, shape="arrow-head",message=None):
        pass
    
    def __str__(self):
        if not message:
            return f"{origin.id} {LINK_SHAPES[self.shape]} {end.id}"
        else:
            return f"{origin.id} {LINK_SHAPES[self.shape]} |{message}| {end.id}"
