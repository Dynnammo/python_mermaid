from python_mermaid.diagram import StateDiagram
from python_mermaid.node import StateNode
from python_mermaid.link import StateLink

sleep = StateNode("Sleep")
breakfast = StateNode("Eat breakfast")
work = StateNode("Go to work")
fun = StateNode("Have fun")
lunch = StateNode("Eat lunch")
work_again = StateNode("Work again")
visit_parents = StateNode("Visit parents")
dinner = StateNode("Eat dinner")

m = StateDiagram(
    type="statechart",
    nodes=[sleep, breakfast, work, fun, lunch, work_again, visit_parents, dinner],
    links=[
        StateLink(sleep, breakfast),
        StateLink(breakfast, work, "Working day"),
        StateLink(work, lunch, "Have time for lunch"),
        StateLink(work, work_again, "No time for lunch"),
        StateLink(work_again, dinner),
        StateLink(dinner, sleep),
        StateLink(breakfast, fun, "Weekend"),
        StateLink(fun, lunch),
        StateLink(lunch, visit_parents),
        StateLink(visit_parents, dinner),
    ],
)

m.add_start_and_end_nodes(breakfast, None)
print(m)
