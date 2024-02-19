
"""
A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.

thisset = {"apple", "banana", "cherry"}
print(thisset)

"""

"""
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes an element from the set
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others
"""

"""
1. add(element)
Adds an element to the set.

"""

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}


"""
2. clear()
Removes all elements from the set.
"""
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # Output: set()

"""
3. copy()
Returns a shallow copy of the set.
"""

my_set = {1, 2, 3}
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

"""
4. difference(*others)
Returns the difference between the set and one or more other sets
"""

set1 = {1, 2, 3}
set2 = {2, 3, 4}
difference = set1.difference(set2)
print(difference)  # Output: {1}

"""
5. difference_update(*others)
Removes all elements of other sets from this set.
"""
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1)  # Output: {1}


"""
6. discard(element)
Removes an element from the set if it is a member. (Do nothing if the element is not in the set).
"""

my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

"""
6. discard(element)
Removes an element from the set if it is a member. (Do nothing if the element is not in the set).

"""

my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}


"""
7. intersection(*others)
Returns the intersection of the set with one or more other sets.
"""
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1.intersection(set2)
print(intersection)  # Output: {2, 3}


"""
8. intersection_update(*others)
Updates the set with the intersection of itself with one or more other sets.

"""

set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1)  # Output: {2, 3}


"""
9. isdisjoint(other)
Returns True if two sets have no elements in common.
"""
set1 = {1, 2, 3}
set2 = {4, 5, 6}
disjoint = set1.isdisjoint(set2)
print(disjoint)  # Output: True

"""
10. issubset(other)
Returns True if another set contains this set.

"""
set1 = {1, 2}
set2 = {1, 2, 3, 4}
subset = set1.issubset(set2)
print(subset)  # Output: True

"""
11. issuperset(other)
Returns True if this set contains another set.
"""
set1 = {1, 2, 3, 4}
set2 = {1, 2}
superset = set1.issuperset(set2)
print(superset)  # Output: True

"""
12. pop()
Removes and returns an arbitrary element from the set. Raises KeyError if the set is empty.

"""

my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output: 1, 2, or 3

"""
13. remove(element)
Removes an element from the set. Raises KeyError if the element is not present.
"""

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

"""
14. symmetric_difference(other)
Returns the symmetric difference of two sets
"""

set1 = {1, 2, 3}
set2 = {2, 3, 4}
symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)  # Output: {1, 4}

"""
15. symmetric_difference_update(other)
Updates the set with the symmetric difference of itself with another set.
"""
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 4}

"""
16. union(*others)
Returns the union of the set with one or more other sets.
"""

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1.union(set2)
print(union)  # Output: {1, 2, 3, 4, 5}

"""
17. update(*others)
Updates the set with the union of itself with one or more other sets.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
