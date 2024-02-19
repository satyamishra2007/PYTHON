my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ln = len(my_list)

"""
List comprehension is a concise way to create lists in Python. 
It allows you to create a new list by iterating over an existing iterable (like a list, tuple, string, etc.) and applying an expression to each element. Here's the basic syntax:


new_list = [expression for item in iterable if condition]

expression is the operation or calculation you want to perform on each item.
item is a variable representing each element in the iterable.
iterable is the sequence of elements you're iterating over.
condition (optional) is an expression that filters the elements.
Here are some examples to illustrate how list comprehensions work:


"""

# 1. Doubling each element in a list:

original_list = [1, 2, 3, 4, 5]
doubled_list = [x * 2 for x in original_list]
print(doubled_list)  # Output: [2, 4, 6, 8, 10]

# 2. Filtering elements greater than 3:

original_list = [1, 2, 3, 4, 5]
filtered_list = [x for x in original_list if x > 3]
print(filtered_list)  # Output: [4, 5]

# 3. Creating a list of squares:

original_list = [1, 2, 3, 4, 5]
squared_list = [x ** 2 for x in original_list]
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# 4. Creating a list of tuples:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = [(x, y) for x in list1 for y in list2]
print(
    combined_list)  # Output: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

# 5. Converting a string to a list of characters:

string = "hello"
char_list = [char for char in string]
print(char_list)  # Output: ['h', 'e', 'l', 'l', 'o']
