"""
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = { "brand": "Ford", "model": "Mustang","year": 1964 }
print(thisdict)

Properties :
- Keys are unique in nature

"""

# https://www.programiz.com/python-programming/methods/dictionary/copy
"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

"""

# EMPTY Dictionary declaration
my_dict = {}
mydict = dict()

print(my_dict, mydict)


"""
1. clear()
Removes all elements from the dictionary.
"""

my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # Output: {}


"""
2. copy()
Returns a shallow copy of the dictionary.

"""

my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

"""
3. fromkeys(seq[, value])
Creates a new dictionary with keys from seq and values set to value.
"""
keys = ['a', 'b', 'c']
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}


"""
4. get(key[, default])
Returns the value for key if key is in the dictionary, else default
"""

my_dict = {'a': 1, 'b': 2}
value = my_dict.get('a', 0)
print(value)  # Output: 1

"""
5. items()
Returns a new view of the dictionary's items (key-value pairs).
"""
my_dict = {'a': 1, 'b': 2}
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2)])

"""
6. keys()
Returns a new view of the dictionary's keys.
"""
my_dict = {'a': 1, 'b': 2}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b'])

"""
7. pop(key[, default])
Removes the specified key and returns its associated value. If key is not found, default is returned if given, otherwise a KeyError is raised.
"""

my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
print(value)  # Output: 1

"""
8. popitem()
Removes and returns an arbitrary (key, value) pair from the dictionary.
"""
my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()
print(item)  # Output: ('b', 2)

"""
9. setdefault(key[, default])
Returns the value for key if key is in the dictionary, else sets default as the value for key and returns default
"""

my_dict = {'a': 1, 'b': 2}
value = my_dict.setdefault('c', 0)
print(value)  # Output: 0

"""
10. update([other])
Updates the dictionary with key-value pairs from other, overwriting existing keys if present.
"""

my_dict = {'a': 1, 'b': 2}
other_dict = {'b': 3, 'c': 4}
my_dict.update(other_dict)
print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}

"""
11. values()
Returns a new view of the dictionary's values.
"""

my_dict = {'a': 1, 'b': 2}
values = my_dict.values()
print(values)  # Output: dict_values([1, 2])
