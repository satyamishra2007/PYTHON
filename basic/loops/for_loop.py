my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ln = len(my_list)

print('\n List Traversal using IN Operator')

for num in my_list:
    print(num)

print('\n List Traversal using RANGE Operator')

"""
The range() function generates a sequence of numbers. It can take one, two, or three arguments:
range(stop): Starts from 0 and goes up to (but doesn't include) the specified stop value.
range(start, stop): Starts from start and goes up to (but doesn't include) the specified stop value.
range(start, stop, step): Starts from start, goes up to (but doesn't include) the specified stop value, with increments defined by step

"""

for i in range(ln):
    print(my_list[i])

print("\n")
for i in range(1, 9, 2):
    print(my_list[i])

print("\n")

for i in range(ln, 0, -1):
    print(i)

print('\n List Enumerate')
"""
List Enumerate:
"""

for index, element in enumerate(my_list):
    print(f"Index: {index}, Element: {element}")





