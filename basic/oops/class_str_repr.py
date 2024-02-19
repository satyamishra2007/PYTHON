"""
"""
"""

In Python, the __str__() and __repr__() methods are special methods used to define how an object should be represented as a string. These methods are essential for providing readable representations of objects in different contexts, such as debugging, logging, and user interaction. Let's explore each method and why they are needed:

__str__() Method:
The __str__() method returns the "informal" or "user-friendly" string representation of an object.
It is called when the str() function is invoked on an object or when the object is used in string formatting.
The primary purpose of __str__() is to provide a human-readable representation of an object.
This method is often used for logging, debugging, or displaying information to end-users.

"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Create an instance of Point
point = Point(3, 4)

# Print the object using str()
print(str(point))  # Output: Point(3, 4)


"""
__repr__() Method:
The __repr__() method returns the "official" or "formal" string representation of an object.
It is called when the repr() function is invoked on an object, or when the object is displayed in interactive mode (e.g., in the Python REPL).
The primary purpose of __repr__() is to provide a representation that can be used to recreate the object.
This method is often used for debugging or when you need to produce a string that represents the object's state in a more detailed and precise manner.

"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Create an instance of Point
point = Point(3, 4)

# Print the object using repr()
print(repr(point))  # Output: Point(3, 4)


"""
Use __str__():
User-Facing Output: When you want to provide a readable and user-friendly representation of your objects, especially for end-users or when displaying information in the user interface.
Printing or Logging: When you want the object to display nicely when printed or logged for human consumption.
Informal String Formatting: When you want to use informal string formatting or string interpolation to include objects in strings.


Use __repr__():
Debugging and Development: When you want to provide a detailed and unambiguous representation of your objects for debugging purposes or when developing and testing code.
Interactive Console: When you want the object's representation to be useful when displayed in the interactive console (e.g., in the Python REPL).
Programmatic Use: When you want the representation to be suitable for programmatic use, such as for generating code or scripts.
"""


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer: {self.name}, Email: {self.email}"


customer = Customer("Alice", "alice@example.com")
print(str(customer))  # Output: Customer: Alice, Email: alice@example.com


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(3, 4)
print(repr(point))  # Output: Point(3, 4)

"""
Use Both:
In many cases, it's appropriate to implement both __str__() and __repr__(). __str__() provides a human-readable representation for end-users, while __repr__() provides a more detailed representation for developers and debugging purposes.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


point = Point(3, 4)
print(str(point))  # Output: Point(3, 4)
print(repr(point))  # Output: Point(3, 4)
