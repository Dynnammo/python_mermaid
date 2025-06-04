# Creating a simple flowchart diagram, without any interactions nor style
from python_mermaid.diagram import MermaidDiagram, Node, Link

# Family members
meg = Node("Meg")
jo = Node("Jo")
beth = Node("Beth")
amy = Node("Amy")
robert = Node("Robert March")

the_march_family = [meg, jo, beth, amy, robert]

# Create links
family_links = [
    Link(robert, meg),
    Link(robert, jo),
    Link(robert, beth),
    Link(robert, amy),
]

chart = MermaidDiagram(title="Little Women", nodes=the_march_family, links=family_links)

print(chart)
