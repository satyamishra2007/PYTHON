"""

A tuple is a collection which is ordered and unchangeable.
 In Python tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

These are the only two methods available for tuples in Python. They provide basic functionalities for counting occurrences of values and finding the index of specific values.
"""

"""
Tuples in Python are immutable sequences, so they have fewer methods compared to lists. Here are all the methods available for tuples:

count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
Test Yourself With Exercises
"""

"""
1. count(value)
Returns the number of occurrences of a specified value in the tuple
"""

my_tuple = (1, 2, 3, 4, 2, 2)
count = my_tuple.count(2)
print(count)  # Output: 3

"""
2. index(value[, start[, stop]])
Returns the index of the first occurrence of a specified value in the tuple.
"""

my_tuple = (1, 2, 3, 4, 2, 2)
index = my_tuple.index(2)
print(index)  # Output: 1



my_tuple = (1, 2, 3, 4, 2, 2)
length = len(my_tuple)
print(length)  # Output: 6