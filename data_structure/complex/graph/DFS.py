"""

"""
"""
Depth-First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking. 
It starts at a selected node (often referred to as the "root" in a tree or the "source" in a graph) and explores as far as 
possible along each branch before backtracking.

How DFS Works:
 1.Start with a stack data structure and push the starting node onto the stack.
 2.While the stack is not empty:
    - Pop a node from the top of the stack.
    - Visit the popped node.
    - Push all its unvisited adjacent nodes onto the stack.
 3.Repeat this process until the stack is empty.

"""

from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def dfs(self, start):
        visited = set()
        stack = [start]  # Initialize stack with starting vertex

        while stack:
            vertex = stack.pop()  # Pop the top vertex from the stack
            if vertex not in visited:
                print(vertex, end=' ')  # Visit the vertex
                visited.add(vertex)

                # Push unvisited neighbors onto the stack
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)


# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("DFS Traversal:")
graph.dfs(0)
