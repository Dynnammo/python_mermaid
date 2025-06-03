from python_mermaid.diagram import StateDiagram, MermaidDiagram
from .utils import *

def test_setup_diagram_with_only_a_title():
    m = StateDiagram(title=DUMMY_TITLE)
    assert str(m) == simple_diagram

def test_diagram_with_only_a_node():
    m = StateDiagram(title=DUMMY_TITLE, nodes=[NODE_2], type="statechart")
    # import pdb; pdb.set_trace()
    assert str(m) == diagram_with_one_node

def test_diagram_with_multiple_nodes():
    m1 = StateDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_2, NODE_3], 
        type="statechart"
    )
    assert(len(m1.graph.nodes) == 2)
    assert str(m1) == diagram_with_multiple_nodes
    #Test that node without description is not reported
    m2 = StateDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1, NODE_2], 
        type="statechart"
    )
    assert(len(m2.graph.nodes) == 2)
    assert str(m2) == diagram_with_one_node

def test_adding_nodes_to_diagram():
    m = StateDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_2],
        type="statechart"
    )
    m.add_nodes([NODE_3])
    assert(len(m.graph.nodes) == 2)
    assert str(m) == diagram_with_multiple_nodes
    
def test_diagram_with_nodes_and_links():
    m = StateDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1, NODE_2, NODE_3],
        links=[LINK_1, LINK_2, LINK_3],
        type="statechart"
    )
    assert str(m) == diagram_with_nodes_and_links

def test_diagram_with_start_end_nodes():
    m = StateDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1, NODE_2, NODE_3],
        links=[LINK_1, LINK_2, LINK_3],
        type="statechart"
    )
    m.add_start_and_end_nodes(NODE_2, NODE_3)
    assert str(m) == diagram_with_start_end_node

def test_adding_links_to_diagram():
    m = StateDiagram(
        title=DUMMY_TITLE,
        nodes=[NODE_1, NODE_2, NODE_3],
        links=[LINK_1],
        type="statechart"
    )
    m.add_links([LINK_2, LINK_3])
    assert str(m) == diagram_with_nodes_and_links

def test_diagram_with_short_comment():
    n = StateNode(NODE_2.id, NODE_2.content)
    n.add_note("This is a short comment")
    m = StateDiagram(title=DUMMY_TITLE, nodes=[n], type="statechart")
    assert str(m) == diagram_with_short_comment

def test_diagram_with_long_comment():
    n = StateNode(NODE_2.id, NODE_2.content)
    n.add_note("This is a long comment\nwith second line")
    m = StateDiagram(title=DUMMY_TITLE, nodes=[n], type="statechart")
    assert str(m) == diagram_with_long_comment

# def test_adding_links_to_diagram():
#     m = MermaidDiagram(
#         title=DUMMY_TITLE,
#         nodes=[NODE_1, NODE_2],
#         links=[LINK_1, LINK_2],
#     )
#     assert str(m) == diagram_with_nodes_and_links
#     m.add_links([LINK_3])
#     assert str(m) == (
#         diagram_with_nodes_and_links + f"\n{str(LINK_3)}"
#     )

# def test_diagram_with_subgraph():
#     m = MermaidDiagram(
#         title=DUMMY_TITLE,
#         nodes=[BIG_NODE_1,NODE_2]
#     )
#     assert str(m) == diagram_with_subgraphs

def test_diagram_without_title():
    m = StateDiagram(type="statechart")
    assert str(m) == diagram_without_title
