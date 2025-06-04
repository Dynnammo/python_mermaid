# Python-Mermaid
This modules aims to implement a simple way for developers/admin-sys/devops to create on-the-fly [Mermaid diagrams](https://mermaid.js.org/).

✅ Use of this module when:
- keeping up-to-date diagrams about systems that can can be discovered with automated scripts :
    - architecture of a server (packages, services,...)
    - architecture of a folder (files and subfolders,...)
- keeping up-to-date diagrams about a data-visualization tool (like [Metabase](https://metabase.com), [Lightdash](https://lightdash.com) etc.)
    - list of collections and indicators with their links for modification


❌ Do not use this module for
- making a single instance diagram that doesn't need to be updated : documentation, presentation etc.

## Installation
```shell
pip install python_mermaid
```

## How to use
All examples are available [here](./examples)

Run the script below to see diagram generation
```py
# Creating a simple flowchart diagram
from python_mermaid.diagram import (
    MermaidDiagram,
    Node,
    Link
)

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

chart = MermaidDiagram(
    title="Little Women",
    nodes=the_march_family,
    links=family_links
)

print(chart)
```

Returns the following
```txt
---
title: Little Women
---
graph TD
meg["Meg"]
jo["Jo"]
beth["Beth"]
amy["Amy"]
robert_march["Robert March"]
robert_march ---> meg
robert_march ---> jo
robert_march ---> beth
robert_march ---> amy
```
which results can be seen [here](https://mermaid.live/edit#pako:eNptj8FOw0AMRH9l5XPzA3tAAnFC9AIHpOIKuYlJUmo72jqHqOq_46zEiZzGbzzS2DdorWPI0DQNqo9-4ZxeRw9NHyasqHXTF5qGhCrcfyLsuUc4op4t4MXqfGIfgp5CKpMsgY-yVCp24uJfQqVdU28V037Ff_sUjQ8pmrbss225a_mWH0fADoSL0NjFlzfUlBB8YGGEHGNH5QcB9R45mt3eF20he5l5B_PUkfPzSPG9QP6myzXcifRg9sf3X1ADb2E)

## Roadmap
### October 2023
1-to-1 implementation of [flowchart](https://mermaid.js.org/syntax/flowchart.html#flowcharts-basic-syntax)
- [ ] All features of flowchart
    - [x] Chart title
    - [x] Nodes shapes
    - [x] Links between nodes
    - [x] Subgraph
        - [ ] Links between nodes with subgraphs
        - [ ] Directions ([#24](https://github.com/Dynnammo/python_mermaid/issues/24))
    - [ ] Interaction
    - [ ] Styling and classes ([#19](https://github.com/Dynnammo/python_mermaid/issues/19) and [#20](https://github.com/Dynnammo/python_mermaid/issues/20))
    - [ ] Basic support for fontawesome ([#23](https://github.com/Dynnammo/python_mermaid/issues/23))

### November 2023
- [ ] Main Features of stateflow-v2
    - [x] Nodes
    - [x] Notes
    - [x] Start and End nodes
    - [x] Named links between nodes
    - [ ] Graph configuration

### End 2023
- [ ] Architecture improvements for easing diagram creation
## Development
- Requirements: install [Poetry](https://python-poetry.org). Here is the official method below. ⚠️ Please consider getting a look at Poetry's documentation if it doesn't work. ⚠️
```shell
curl -sSL https://install.python-poetry.org | python3 -
```
- All-in-one command below to clone and install dependencies
```shell
curl -sSL https://install.python-poetry.org | python3 -
git clone https://github.com/Dynnammo/python_mermaid
cd python_mermaid
poetry shell
poetry install --with dev
```

### Quick commands
- Launch tests: `poetry run pytest`
- Check linting: `poetry run ruff check .`
- Check typing: `poetry run mypy python_mermaid`
```

To check linting:
```shell
poetry run flake8
```

This project comes with a tool called [`pre-commit`](https://pre-commit.com/) that checks if your code is correctly linted.
If you want to use it, run the following
```shell
pre-commit install
```

## Contribute
Wanna help ? Find a bug ?
1. Do not hesitate to fork the repository and send PRs with your changes
2. No time to code ? Send a bug/feature issue [here](https://github.com/Dynnammo/python_mermaid/issues/new/choose)