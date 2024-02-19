

"""
A stack is a fundamental data structure in computer science that follows the Last In, First Out (LIFO) principle. It can be imagined as a stack of plates where you can only add or remove plates from the top. In Python, you can implement a stack using a list with a few simple operations. Let's explore the stack data structure and its operations in detail:

Stack Operations:
Push: Adds an item to the top of the stack.
Pop: Removes and returns the item at the top of the stack.
Peek (or Top): Returns the item at the top of the stack without removing it.
IsEmpty: Checks if the stack is empty.
Size: Returns the number of items in the stack.

Implementation of Stack in Python:

"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Create an empty stack
stack = Stack()

# Push items onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Check the top item
print("Top item:", stack.peek())  # Output: 3

# Pop items from the stack
print("Popped item:", stack.pop())  # Output: 3
print("Popped item:", stack.pop())  # Output: 2

# Check if the stack is empty
print("Is stack empty?", stack.is_empty())  # Output: False

# Get the size of the stack
print("Stack size:", stack.size())  # Output: 1

"""
Time Complexity:
- The time complexity for all stack operations (push, pop, peek, is_empty, size) is O(1).
- This is because these operations involve accessing or modifying the top of the stack, which can be done in constant time regardless of the size of the stack.

Stack Applications:
- Function call stack in programming languages (for function calls and returns).
- Expression evaluation and parsing (e.g., infix to postfix conversion).
- Backtracking algorithms (e.g., depth-first search).
- Undo functionality in text editors and command-line interfaces.
"""


stack = ['satya', 'mishra', 'jeypore', 'swati', 'mishra', 'puri']

# Traverse
for val in stack:
    print(val)

print('***************')
for i in range(len(stack)):
    print(stack[i])

# push
print('***************')
stack.append("USA")
for val in stack:
    print(val)

# pop

print('***************')
stack.pop()
for val in stack:
    print(val)