"""

"""
"""
A heap queue, commonly known as a priority queue, is a specialized tree-based data structure that is 
used to efficiently maintain a collection of elements where each element has a priority assigned to it. 
Priority queues are often implemented using a binary heap, which is a complete binary tree 
where the value of each parent node is greater than or equal to the values of its children (max heap) 
or less than or equal to the values of its children (min heap). 
Priority queues support efficient insertion and extraction of elements based on their priority.

In Python, the heapq module provides functions to create and manipulate heap queues using lists. 
Here's how you can use heapq to work with heap queues
"""

"""
Key Operations Provided by heapq:
heappush(heap, item):

Inserts the item onto the heap.
Time Complexity: O(log n), where n is the number of elements in the heap.
heappop(heap):

Removes and returns the smallest element from the heap.
Time Complexity: O(log n), where n is the number of elements in the heap.
heappushpop(heap, item):

Pushes item onto the heap and then pops and returns the smallest element.
Time Complexity: O(log n), where n is the number of elements in the heap.
heapify(x):

Transforms list x into a heap in-place.
Time Complexity: O(n), where n is the number of elements in the list.
heapreplace(heap, item):

Pops and returns the smallest element from the heap, then pushes item onto the heap.
Time Complexity: O(log n), where n is the number of elements in the heap.
nlargest(n, iterable):

Returns the n largest elements from the iterable.
Time Complexity: O(n log k), where n is the number of elements in the iterable and k is the value of n.
nsmallest(n, iterable):

Returns the n smallest elements from the iterable.
Time Complexity: O(n log k), where n is the number of elements in the iterable and k is the value of n.

"""

"""
Usage in Real-World Problem Statements:
Priority Queues:

Heap queues are commonly used to implement priority queues, where elements with higher priority are processed before elements with lower priority. For example, in task scheduling algorithms, jobs with higher priority are executed first.
Graph Algorithms:

Heap queues are used in various graph algorithms such as Dijkstra's algorithm for finding shortest paths, Prim's algorithm for minimum spanning trees, and Kruskal's algorithm for finding minimum spanning trees.
Merge K Sorted Lists:

In scenarios where you have k sorted lists and you need to merge them into a single sorted list, heap queues can be used to efficiently merge the lists.
Top K Elements:

Heap queues are useful for finding the top k elements from a large dataset. For example, finding the top k most frequent elements in a stream of data.
Priority-Based Scheduling:

Heap queues can be used in scheduling algorithms where tasks or jobs are executed based on their priority levels, ensuring efficient resource allocation.


"""

"""
Example 1: heappush(heap, item)
Explanation: In this example, we initialize an empty heap and then use heapq.heappush() to insert elements into the heap. 
The resulting heap becomes [3, 5, 7].

"""

import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)

print("Heap after push operations:", heap)  # Output: [3, 5, 7]

"""
Example 2: heappop(heap)
Explanation: In this example, we have a heap [3, 5, 7], and we use heapq.heappop() to extract the smallest element from the heap. 
The smallest element (3) is extracted, and the resulting heap becomes [5, 7].

"""

heap = [3, 5, 7]
min_value = heapq.heappop(heap)

print("Min value extracted:", min_value)  # Output: 3
print("Heap after pop operation:", heap)  # Output: [5, 7]

"""
Example 3: heappushpop(heap, item)

Explanation: In this example, we have a heap [3, 5, 7], and we use heapq.heappushpop() to push the element 2 onto the heap 
and then pop and return the smallest element. 
The smallest element (3) is popped, and 2 becomes the new root of the heap.

"""


heap = [3, 5, 7]
min_value = heapq.heappushpop(heap, 2)

print("Min value after push-pop operation:", min_value)  # Output: 2
print("Heap after push-pop operation:", heap)  # Output: [3, 5, 7]

"""
Example 4: heapify(x)

Explanation: In this example, we have a list [5, 3, 7], and we use heapq.heapify() to transform the list into a heap in-place. 
The resulting heap becomes [3, 5, 7].


"""

import heapq

x = [5, 3, 7]
heapq.heapify(x)

print("Heapified list:", x)  # Output: [3, 5, 7]

"""
Example 5: heapreplace(heap, item)
Explanation: In this example, we have a heap [3, 5, 7], and we use heapq.heapreplace() to pop and return the smallest 
element from the heap and then push the new element 2 onto the heap. The smallest element (3) is replaced with 2, 
and the resulting heap becomes [2, 5, 7].



"""

import heapq

heap = [3, 5, 7]
min_value = heapq.heapreplace(heap, 2)

print("Min value after replace operation:", min_value)  # Output: 3
print("Heap after replace operation:", heap)  # Output: [2, 5, 7]

"""
Example 6: nlargest(n, iterable)
Explanation: In this example, we have a list of numbers [5, 3, 7, 2, 8], 
and we use heapq.nlargest() to find the three largest numbers from the list. The three largest numbers are [8, 7, 5]

"""

import heapq

numbers = [5, 3, 7, 2, 8]
largest_three = heapq.nlargest(3, numbers)

print("Three largest numbers:", largest_three)  # Output: [8, 7, 5]

"""
Example 7: nsmallest(n, iterable)
Explanation: In this example, we have a list of numbers [5, 3, 7, 2, 8], 
and we use heapq.nsmallest() to find the three smallest numbers from the list. The three smallest numbers are [2, 3, 5].
"""
import heapq

numbers = [5, 3, 7, 2, 8]
smallest_three = heapq.nsmallest(3, numbers)

print("Three smallest numbers:", smallest_three)  # Output: [2, 3, 5]
