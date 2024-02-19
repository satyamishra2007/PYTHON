"""
"""

"""
In Python, the collections module provides a specialized data structure called deque, which stands for "double-ended queue". 
A deque is similar to a regular queue but supports efficient insertion and deletion operations at both ends of the queue. 
This makes it suitable for scenarios where items need to be added or removed from both the front and the back of the queue efficiently. 
Let's explore the differences between a regular queue and a deque:

Differences between Queue and Deque:
1.Insertion and Deletion Efficiency:

- In a regular queue implemented using a list, adding or removing an item from the front of the queue (using pop(0) or insert(0, item)) has a time complexity of O(n) because it requires shifting all remaining elements.
- In a deque, adding or removing items from both ends of the deque has a time complexity of O(1), making it more efficient.

2.Data Structure Design:

- A queue is typically implemented using a list with the front of the queue at index 0 and the rear at the end of the list.
- A deque is specifically designed to efficiently support insertion and deletion at both ends, offering optimized performance for these operations.


append(x): Add element x to the right end of the deque.

appendleft(x): Add element x to the left end of the deque.

clear(): Remove all elements from the deque.

count(x): Count the number of occurrences of x in the deque.

extend(iterable): Extend the right end of the deque by appending elements from the iterable.

extendleft(iterable): Extend the left end of the deque by appending elements from the iterable. Note that the elements are added in reverse order.

index(x, start, end): Return the index of the first occurrence of x in the deque within the specified start and end indices.

insert(i, x): Insert element x at position i in the deque.

pop(): Remove and return the rightmost element from the deque. Raises an IndexError if the deque is empty.

popleft(): Remove and return the leftmost element from the deque. Raises an IndexError if the deque is empty.

remove(value): Remove the first occurrence of value from the deque. Raises a ValueError if the value is not present.

reverse(): Reverse the elements of the deque in place.

rotate(n): Rotate the deque n steps to the right. If n is negative, rotate to the left.

maxlen: Maximum size of the deque, or None if there is no limit.


"""
from collections import deque

# Create a deque
my_deque = deque([1, 2, 3, 4])

# Append an element to the right end
my_deque.append(5)

# Append an element to the left end
my_deque.appendleft(0)

# Extend the deque from the right end
my_deque.extend([6, 7, 8])

# Extend the deque from the left end
my_deque.extendleft([-1, -2])

print("Deque:", my_deque)

# Remove and return the rightmost element
rightmost = my_deque.pop()
print("Rightmost:", rightmost)

# Remove and return the leftmost element
leftmost = my_deque.popleft()
print("Leftmost:", leftmost)

# Rotate the deque to the right
my_deque.rotate(2)
print("Rotated deque:", my_deque)

# Reverse the elements of the deque
my_deque.reverse()
print("Reversed deque:", my_deque)


"""
Advantages of Using Deque:
Efficient insertion and deletion at both ends of the deque.
Suitable for implementing queues, stacks, and double-ended queues.
Optimized performance for scenarios requiring frequent insertion and deletion operations at both ends.

In summary, while both regular queues and deques serve similar purposes, 
deques provide superior performance for insertion and deletion operations at both ends, 
making them a preferred choice in scenarios requiring such operations to be performed efficiently.


"""
