"""
There are four collection data types in the Python programming language:

List  --> is a collection which is ordered and changeable. Allows duplicate members.
Tuple --> is a collection which is ordered and unchangeable. Allows duplicate members.
Set   --> is a collection which is unordered and unindexed. No duplicate members.
Dictionary--> is a collection which is unordered, changeable and indexed. No duplicate members.
When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

"""

"""
A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
mylist = ["apple", "banana", "cherry"]
print(mylist)

"""

"""
LIST METHODS:

append(): Adds an element to the end of the list.
extend(): Extends the list by appending elements from another list.
insert(): Inserts an element at a specified index.
remove(): Removes the first occurrence of a value.
pop(): Removes and returns the element at a specified index.
index(): Returns the index of the first occurrence of a value.
count(): Returns the number of occurrences of a value.
sort(): Sorts the list in ascending order.
reverse(): Reverses the order of elements in the list.
"""

"""
1. append(x)
Time Complexity: O(1)
Space Complexity: O(1)
"""
my_list = list([1, 2, 3])
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

"""
2. extend(iterable)
Time Complexity: O(k)
Space Complexity: O(k)
"""

my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

"""
3. insert(i, x)
Time Complexity: O(n)
Space Complexity: O(1)
"""
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # Output: [1, 5, 2, 3]

"""
4. remove(x)
Time Complexity: O(n)
Space Complexity: O(1)
"""
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]

"""
5. pop([i])
Time Complexity: O(n)
Space Complexity: O(1)
"""
my_list = [1, 2, 3]
element = my_list.pop(1)
print(element)  # Output: 2
print(my_list)  # Output: [1, 3]

"""
6. index(x[, start[, end]])

The index() method in Python returns the index of the first occurrence of a specified value in a list. It takes the following syntax:

python
Copy code
list.index(value, start, stop)
value: The value to search for in the list.
start (optional): The index from where the search begins. Defaults to 0.
stop (optional): The index where the search ends. Defaults to the end of the list.

Time Complexity: O(n)
Space Complexity: O(1)
"""
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1

"""
7. count(x)
Time Complexity: O(n)
Space Complexity: O(1)
"""

my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2

"""
8. sort(key=None, reverse=False)
Time Complexity: O(n log n)
Space Complexity: O(log n) to O(n)
"""

my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

my_list.sort(reverse=True)
print(my_list)  # Output: [3,2,1]


"""
9. reverse()
Time Complexity: O(n)
Space Complexity: O(1)
"""

my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]

"""
10. copy()
Time Complexity: O(n)
Space Complexity: O(n)
"""

my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]

"""
11. clear()

Time Complexity: O(1)
Space Complexity: O(1)

"""

my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []
