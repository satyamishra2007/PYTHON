"""

"""

"""
A lambda function in Python is a small anonymous function defined using the lambda keyword. 
It can have any number of arguments but only one expression. 
Lambda functions are useful when you need a simple function for a short period of time, often for use as arguments in higher-order functions like map(), filter(), and sorted(). Here's an explanation with examples

lambda arguments: expression

"""

"""

Example 1: Simple Lambda Function
"""

# Define a lambda function that adds two numbers
add = lambda x, y: x + y

# Call the lambda function
result = add(3, 5)
print(result)  # Output: 8

"""
Example 2: Use with Built-in Functions (map, filter, sorted)

"""

# Use lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Use lambda with filter()
numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # Output: [2, 4]

# Use lambda with sorted()
students = [{'name': 'John', 'age': 25}, {'name': 'Alice', 'age': 20}, {'name': 'Bob', 'age': 30}]
sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)
# Output: [{'name': 'Alice', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Bob', 'age': 30}]

"""
Example 3: Use in Higher-Order Functions
"""


# Define a function that takes another function as argument and applies it to a value
def apply_func(func, value):
    return func(value)


# Use apply_func with a lambda function
result = apply_func(lambda x: x * 2, 5)
print(result)  # Output: 10

"""
Example 4: Use with Conditional Expressions
"""

# Use lambda with conditional expression
even_or_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd'
print(even_or_odd(4))  # Output: Even
print(even_or_odd(3))  # Output: Odd


"""
Advanced Details:
Lambdas are anonymous functions; they don't have a name and are defined inline.
Lambdas can take any number of arguments but can only have one expression.
Lambdas are often used with higher-order functions and in functional programming paradigms.
While lambdas are powerful, they are generally used for simple operations. For more complex functions, it's recommended to define regular named functions for better readability and maintainability.
"""