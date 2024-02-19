"""
"""

"""
Adjacency List Representation:
In the adjacency list representation, each vertex in the graph is associated with a list of its neighboring vertices. 
This representation is often used for sparse graphs where the number of edges is much smaller than the maximum possible edges.

Here's how to represent a graph using adjacency lists in Python:

"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)


# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("Graph represented using adjacency lists:")
print(graph.adjacency_list)

"""
Adjacency Matrix Representation:
In the adjacency matrix representation, a 2D matrix is used to represent the connections between vertices. 
Each cell matrix[i][j] represents whether there is an edge from vertex i to vertex j. This representation is often used for dense graphs where the number of edges is close to the maximum possible edges.

Here's how to represent a graph using an adjacency matrix in Python:
"""


class Graph:
    def __init__(self, num_vertices):
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.adjacency_matrix[u][v] = 1
        self.adjacency_matrix[v][u] = 1


# Example usage:
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("Graph represented using adjacency matrix:")
for row in graph.adjacency_matrix:
    print(row)

"""
Summary:
Adjacency List: Suitable for sparse graphs, easy to implement, and efficient for querying neighbors.
Adjacency Matrix: Suitable for dense graphs, efficient for edge existence queries, takes more space but allows constant-time edge weight lookups.


The choice between adjacency lists and adjacency matrices depends on factors like the graph's density, 
the types of operations to be performed (e.g., edge insertion, edge deletion, querying for neighbors), and memory constraints.

"""