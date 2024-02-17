"""


"""
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
thislist = ["apple", "banana", "cherry"]
print(thislist)

"""


"""
LIST METHODS:

list.append(x) : Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable): Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x) : Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x) : Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i]): Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear() :Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]]): Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. 
The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x) :  Return the number of times x appears in the list.

list.sort(*, key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse() : Reverse the elements of the list in place.

list.copy() : Return a shallow copy of the list. Equivalent to a[:].

"""


nums = [1, 2, 3, 4, 5, 6, 7]

nums.append(8)
print(nums)
print(nums.index(4))

print(f"Length of list is : {len(nums)}")
nums.append(4)

print(f"Number occurrence for 4 is: {nums.count(4)}")
print(f"Number occurrence for 4 is: {nums.count(10)}")


print(f"Index of 4 is: {nums.index(4)}")
