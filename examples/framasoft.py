# Using a wonderful french association to demonstrate interactions and subgraph
from python_mermaid.diagram import (
    MermaidDiagram,
    Node,
    Interaction
)


framatools = {
    "practical_tools": [
        "Framaforms",
        "Framindmap",
        "Framacart"
    ],
    "exchange_tools": [
        "Framatalk",
        "Framalistes",
        "Framateam"
    ],
    "entertainment_tools": [
        ("Framinetest Édu", "https://framinetest.org"),
    ],
    "organizing_tools": [
        "Framadate",
        "Framagenda",
        "Framavox",
        "Mobilizon"
    ],
    "collaborating_tools": [
        "Framacalc",
        "Framapad"
    ],
    "developing_tools": [
        "Framagit"
    ]
}

nodes = []
interactions = []
for group, tools in framatools.items():
    node_group = Node(group)
    for tool in tools:
        if isinstance(tool, tuple):
            node_tool = Node(tool[0])
            interactions.append(Interaction(node_tool, args=[tool[1]]))
        else:
            node_tool = Node(tool)
            interactions.append(
                Interaction(
                    node_tool,
                    args=[f"\"https://{node_tool.id}.org\""]
                )
            )
        node_group.add_sub_nodes([node_tool])
    nodes += [node_group]

m = MermaidDiagram(
    title="Framaverse",
    nodes=nodes,
    interactions=interactions
)

print(m)
