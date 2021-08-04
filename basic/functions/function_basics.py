def greet(*args,**kwargs):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in args:
        print("Hello", name)

    #print(args,kwargs)
    for k,v in kwargs.items():
        print(kwargs[k])

greet("Monica", "Luke", "Steve", "John",name="Monica",age=12)


#
# #RECURSION
# def factorial(num):
#     if num ==1:       # BASE CONDITION to EXIT
#         return 1
#     else:
#         result = num * factorial(num -1)
#     return result
#
# print(factorial(5))
#
#
# #lambda
#
# double = lambda x: x * 2
# print(double(5))
#
#
# """
# The filter() function in Python takes in a function and a list as arguments.
# The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
# Here is an example use of filter() function to filter out only even numbers from a list.
#
# """
# complete_list = [1,2,3,4,5,6,7,8,9]
# even_list = list(filter(lambda x:(x % 2),complete_list))
# print(even_list)
#
#
#
# complete_list = [1,2,3,4,5,6,7,8,9]
# lambda_list = list((lambda x:(x % 2),complete_list))
# print(lambda_list)
#
#
#
#
#
#
#
# """
# Example use with map()
# The map() function in Python takes in a function and a list.
#
# The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.
#
# Here is an example use of map() function to double all the items in a list.
#
# """
# complete_list = [1,2,3,4,5,6,7,8,9]
#
# multiply_list = list(map(lambda x: x * 2,complete_list ))
# print(multiply_list)
#
#
