
"""
"""
"""
A queue is a fundamental data structure in computer science that follows the First In, First Out (FIFO) principle. 
It can be imagined as a line of people waiting for a service where the person who has been waiting the longest is the first to be served. 
In Python, you can implement a queue using a list with a few simple operations. 
Let's explore the queue data structure and its operations in detail:

Queue Operations:
Enqueue (or Push): Adds an item to the end of the queue.
Dequeue (or Pop): Removes and returns the item at the front of the queue.
Front: Returns the item at the front of the queue without removing it.
IsEmpty: Checks if the queue is empty.
Size: Returns the number of items in the queue.

Implementation of Queue in Python:


"""


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def front(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

"""
Example Usage:

"""

# Create an empty queue
queue = Queue()

# Enqueue items into the queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Check the front item
print("Front item:", queue.front())  # Output: 1

# Dequeue items from the queue
print("Dequeued item:", queue.dequeue())  # Output: 1
print("Dequeued item:", queue.dequeue())  # Output: 2

# Check if the queue is empty
print("Is queue empty?", queue.is_empty())  # Output: False

# Get the size of the queue
print("Queue size:", queue.size())  # Output: 1

"""
Time Complexity:
- The time complexity for enqueue and dequeue operations in a queue implemented using a list is O(1).
- However, when using a list, the dequeue operation has a time complexity of O(n) because it requires shifting all remaining elements after removing the first element.
Queue Applications:
- Process scheduling in operating systems (e.g., CPU scheduling).
- Task management systems (e.g., task queues in web applications).
- Breadth-first search (BFS) algorithm for graph traversal.
- Print spooling in printers.
- Asynchronous programming and event handling.
Queues are widely used in computer science and software development due to their simplicity, efficiency, and applicability in solving many real-world problems involving sequential processing of data.
"""