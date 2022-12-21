# Python-Mermaid
This modules aims to implement a simple way for developers/admin-sys/devops to create on-the-fly [Mermaid diagrams](https://mermaid.js.org/).

## Installation
```shell
pip install python_mermaid
```

## Getting started
```py
# Creating a simple flowchart diagram
from python_mermaid import FlowChart

the_march_family = [
    ("Meg","M"),
    ("Jo", "J"),
    ("Beth"."B"),
    ("Amy", "A"),
    ("Robert March","RM")
]

links = [
    ("Robert March", "Meg"),
    ("Robert March", "Jo"),
    ("Robert March", "Beth"),
    ("Robert March", "Amy"),
]

chart = Flowchart(
    title="Little Women",
    nodes=the_march_family,
    links=links
)

print(chart)
```
Returns the following
```txt
---
title: "Little Women"
---
graph LR
M["Meg"]
J["Jo"]
B["Beth"]
A["Amy"]
RM["Robert"]

RM --> M
RM --> J
RM --> B
RM --> A
```
which results can be seen [here](https://mermaid.live/edit#pako:eNo9jr0KgzAQgF8l3GxewKGgdBJd7FBor0OqV5U2iaTnIOK79xKo2_fdD3wbdL4nyEFrjY4n_lCuEOqJhdTVW3II6NJ2CGYeVd2ia-4IDQ0ID3SVcOUTloIl8ZikECnsmriND61_UuDkcaK0PqnmoOqg8qACMrAUrJl6KdzQKUnjkSwhxMrehHes2-XOLOwvq-sg57BQBsvcG6bzZKTaQv4yn69MZ-Nu3v99_wEheFGF)


## Roadmap
- [ ] **flowchart** setup
- [ ] Add *styles* for nodes or links
- [ ] More diagrams !

## Contribute
Wanna help ? Find a bug ?
1. Do not hesitate to fork the repository and send PRs with your changes
2. No time to code ? Send a bug/feature issue [here](https://github.com/Dynnammo/python_mermaid/issues/new/choose)