# Python Graph Implementation

This project provides a simple Python implementation of a **Graph** data structure, supporting both **directed** and **undirected** graphs. It allows for creating nodes, adding edges, and traversing the graph using common algorithms.

## Features

- Create a graph using an adjacency list representation.
- Add nodes and edges dynamically.
- Support for **directed** and **undirected** graphs.
- Graph traversal methods:
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
- Optionally, support weighted graphs (if implemented).

## Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/python-graph-implementation.git
cd python-graph-implementation

    Make sure you have Python 3.x installed. You can check with:

python --version

No additional packages are required for the basic implementation.
Usage

from graph import Graph

# Create a graph (directed=False for undirected)
g = Graph(directed=False)

# Add nodes
g.add_node('A')
g.add_node('B')
g.add_node('C')

# Add edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'C')

# Display the graph
g.display()

# Perform BFS and DFS
print("BFS Traversal from A:", g.bfs('A'))
print("DFS Traversal from A:", g.dfs('A'))

Methods
Method	Description
add_node()	Adds a new node to the graph.
add_edge()	Adds an edge between two nodes.
display()	Prints the adjacency list of the graph.
bfs(start)	Performs Breadth-First Search from a node.
dfs(start)	Performs Depth-First Search from a node.
Example Output

Graph adjacency list:
A -> B, C
B -> A, C
C -> A, B

BFS Traversal from A: ['A', 'B', 'C']
DFS Traversal from A: ['A', 'B', 'C']

Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements, such as:

    Adding support for weighted graphs



