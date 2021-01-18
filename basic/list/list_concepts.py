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
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

"""



#Nested List
n_list = ["Happy", [2, 0, 1, 5]]
print(n_list[0][1])

my_list = [1, 3, 5, 9, 7, 5]
print(my_list[:])
my_list.pop(1)
print(my_list)