"""

"""

"""
In a singly linked list, each node contains a reference to the next node in the sequence.

Head -> [Data | Next] -> [Data | Next] -> [Data | Next] -> None
Here, each node ([Data | Next]) contains the data and a reference (Next) to the next node in the list. Traversal is possible only in one direction, starting from the head.

Operations on Singly Linked List:
Insertion:

Append: Insert an element at the end of the list.
- Insert at Beginning: Insert an element at the beginning of the list.
- Insert after Node: Insert an element after a specific node.
- Insert at Position: Insert an element at a specific position in the list.

Deletion:

- Delete at Beginning: Remove the first element from the list.
- Delete at End: Remove the last element from the list.
- Delete by Value: Remove a specific element from the list.
- Delete by Position: Remove an element at a specific position in the list.

Traversal:

- Display: Display all elements of the list.
- Search: Search for a specific element in the list.

Time Complexity:

- Insertion/Deletion at Beginning: O(1)
- Insertion/Deletion at End: O(n)
- Insertion/Deletion at Middle (with traversal): O(n)
- Search: O(n)

Applications:
- Implementing stacks and queues.
- Maintaining a sequence of elements in memory efficiently.
- Implementing hash tables.
- Implementing adjacency lists for graphs.
- Singly linked lists are simple yet powerful data structures that offer flexibility in managing dynamic collections of data. They are widely used in various algorithms and applications due to their efficiency in insertion and deletion operations. However, accessing elements by index is less efficient compared to arrays, as it requires traversal from the head of the list.

"""


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # insert at start, O(1), no traversal
    def insert_at_begin(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # insert at end, O(n), needs traversal
    def insert_at_end(self, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node

    # insert after a given value, O(n), needs traversal
    def insert_after(self, val, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node:
                if curr_node.val == val:
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                curr_node = curr_node.next

    # insert after at index, O(n), needs traversal
    def insert_at(self, ind, val):
        new_node = ListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            count = 0
            curr_node = self.head
            while curr_node:
                if count == ind - 1:
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                count += 1
                curr_node = curr_node.next

    # get size, O()
    def get_size(self):
        if self.head is None:
            return 0
        else:
            curr_node = self.head
            count = 0
            while curr_node:
                count += 1
                curr_node = curr_node.next
            return print(count)

    # remove_at start, O(1)
    def remove_at_begin(self):
        if self.head is None:
            return
        else:
            curr_node = self.head
            self.head = curr_node.next
            curr_node.next = None

    # remove_at_end
    def remove_at_end(self):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node.next.next:
                curr_node = curr_node.next
            curr_node.next = None

    # remove after a value
    def remove(self, val):
        if self.head is None:
            return
        else:
            curr_node = self.head
            while curr_node.next:
                if curr_node.next.val == val:
                    curr_node.next = curr_node.next.next
                curr_node = curr_node.next

    # print list, O(n),needs traversal
    def print_list(self):
        curr_node = self.head
        llst = ''
        while curr_node:
            print(curr_node.val, end=" -> ")
            # llst += str(curr_node.val) + "-->"
            curr_node = curr_node.next
        # return print(llst)


if __name__ == "__main__":
    sll = LinkedList()
    sll.insert_at_begin(20)
    sll.insert_at_begin(10)
    sll.insert_at_end(45)
    sll.print_list()

    print("\n")

    # sll.insert_after(20, 25)
    # sll.insert_at(2, 15)
    sll.get_size()
    print("\n")
    sll.remove_at_begin()
    sll.remove_at_end()
    sll.remove(15)
    sll.print_list()
