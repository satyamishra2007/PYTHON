"""
"""

"""
In Python, *args and **kwargs are special syntax used to pass a variable number of arguments to a function. 
Here's what they mean:

*args:
It allows you to pass a variable number of positional arguments to a function.
The name args is arbitrary; you can use any valid name preceded by an asterisk (*).
Inside the function, args is treated as a tuple containing all the positional arguments passed to the function.

**kwargs:
It allows you to pass a variable number of keyword arguments to a function.
The name kwargs is arbitrary; you can use any valid name preceded by two asterisks (**).
Inside the function, kwargs is treated as a dictionary containing all the keyword arguments passed to the function, where keys are the argument names and values are the argument values.

Combining *args and **kwargs:
You can use both *args and **kwargs in the same function definition. In this case, *args must appear before **kwargs.

"""


def greet(*args, **kwargs):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in args:
        print("Hello", name)

    # print(args,kwargs)
    for k, v in kwargs.items():
        print(kwargs[k])


greet("Monica", "Luke", "Steve", "John", name="Monica", age=12)

"""
Recursive Function
"""


def factorial(num):
    if num == 1:  # BASE CONDITION to EXIT
        return 1
    else:
        result = num * factorial(num - 1)
    return result


print(factorial(5))

"""
lambda anonymous function
"""
double = lambda x: x * 2
print(double(5))

"""
The filter() function in Python takes in a function and a list as arguments.
The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
Here is an example use of filter() function to filter out only even numbers from a list.

"""
complete_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = list(filter(lambda x: (x % 2), complete_list))
print(even_list)

complete_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lambda_list = list((lambda x: (x % 2), complete_list))
print(lambda_list)

"""
Example use with map()
The map() function in Python takes in a function and a list.

The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.

Here is an example use of map() function to double all the items in a list.

"""
complete_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

multiply_list = list(map(lambda x: x * 2, complete_list))
print(multiply_list)
