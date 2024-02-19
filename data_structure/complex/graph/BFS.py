"""

"""

"""
Breadth-First Search (BFS) is a graph traversal algorithm used to explore a graph or tree data structure. 
It starts at a selected node (often referred to as the "root" in a tree or the "source" in a graph) 
and explores all of its neighboring nodes at the present depth before moving on to the nodes at the next depth level. 
This process continues until all nodes have been visited or until the goal node is found. BFS is often used 
to find the shortest path between two nodes in an unweighted graph.

How BFS Works:
1.Start with a queue data structure and enqueue the starting node.
2.While the queue is not empty:
    - Dequeue a node from the front of the queue.
    - Visit the dequeued node.
    - Enqueue all its adjacent nodes that have not been visited yet.
3.Repeat this process until the queue is empty.

"""

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)


# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("\nBFS Traversal using deque:")
graph.bfs(0)


"""

Certainly! We can implement a queue using a simple list in Python. Here's the modified BFS implementation using a list as a queue:
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = [start]  # Using a list as a queue

        while queue:
            vertex = queue.pop(0)  # Dequeue the first element
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                for neighbor in self.adjacency_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)  # Enqueue the neighbor
        print("BFS visited :", visited)

# Example usage:
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3)

print("\nBFS Traversal Using queue:")
graph.bfs(0)
