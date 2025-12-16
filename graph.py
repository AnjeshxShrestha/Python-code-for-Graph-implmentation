class Graph:
    def __init__(self):
        self.graph = {}  # Adjacency list representation

    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, weight):
        """Add an undirected, weighted edge to the graph."""
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        # Add edge in both directions
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def display(self):
        """Print the graph's adjacency list."""
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

# Create a new graph
g = Graph()

n= int(input(" How many edges are there in the Graph? "))
for i in range(n):
    n1=input("Enter start node: ")
    n2=input("Enter end node: ")
    w=int(input("Enter weight between those nodes: "))
    g.add_edge(n1,n2,w)


# Display the graph
g.display()
