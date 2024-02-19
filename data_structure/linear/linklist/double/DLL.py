"""
"""

"""
A doubly linked list is a type of linked list where each node contains a reference (or pointer) 
to the next node in the sequence as well as a reference to the previous node. 
This allows traversal of the list in both forward and backward directions. 
Doubly linked lists offer additional flexibility compared to singly linked lists but require more memory to store the extra pointers.

Head -> [Data | Next, Prev] <-> [Data | Next, Prev] <-> [Data | Next, Prev] -> None

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Append a new node with the given data at the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def display_forward(self):
        """Display all the elements in the linked list in forward direction."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def display_backward(self):
        """Display all the elements in the linked list in backward direction."""
        current = self.tail
        while current:
            print(current.data, end=" -> ")
            current = current.prev
        print("None")


"""
Here's an example of using this doubly linked list:
"""

# Create a new doubly linked list
doubly_linked_list = DoublyLinkedList()

# Append elements to the doubly linked list
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)

# Display the doubly linked list in forward direction
print("Forward:")
doubly_linked_list.display_forward()  # Output: 1 -> 2 -> 3 -> None

# Display the doubly linked list in backward direction
print("Backward:")
doubly_linked_list.display_backward()  # Output: 3 -> 2 -> 1 -> None
