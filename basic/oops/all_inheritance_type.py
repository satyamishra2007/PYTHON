"""
"""

"""
In Python, inheritance allows a class (subclass or child class) to inherit attributes and methods from another class (superclass or parent class). There are different types of inheritance relationships, including single inheritance, multiple inheritance, multilevel inheritance, and hierarchical inheritance. Let's explore each type with examples:
1. Single Inheritance:
Single inheritance involves one subclass inheriting from one superclass.
"""


class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def bark(self):
        return "Woof!"


# Example usage
dog = Dog()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())  # Output: Woof!

"""
2. Multiple Inheritance:
Multiple inheritance involves one subclass inheriting from multiple superclasses.

"""


class A:
    def method_a(self):
        return "Method A"


class B:
    def method_b(self):
        return "Method B"


class C(A, B):
    def method_c(self):
        return "Method C"


# Example usage
obj = C()
print(obj.method_a())  # Output: Method A
print(obj.method_b())  # Output: Method B
print(obj.method_c())  # Output: Method C

"""
3. Multilevel Inheritance:
Multilevel inheritance involves a chain of inheritance where a subclass inherits from another subclass.
"""


class A:
    def method_a(self):
        return "Method A"


class B(A):
    def method_b(self):
        return "Method B"


class C(B):
    def method_c(self):
        return "Method C"


# Example usage
obj = C()
print(obj.method_a())  # Output: Method A
print(obj.method_b())  # Output: Method B
print(obj.method_c())  # Output: Method C

"""
4. Hierarchical Inheritance:
Hierarchical inheritance involves multiple subclasses inheriting from the same superclass.

"""


class Animal:
    def speak(self):
        return "Animal speaks"


class Dog(Animal):
    def bark(self):
        return "Woof!"


class Cat(Animal):
    def meow(self):
        return "Meow!"


# Example usage
dog = Dog()
cat = Cat()
print(dog.speak())  # Output: Animal speaks
print(dog.bark())  # Output: Woof!
print(cat.speak())  # Output: Animal speaks
print(cat.meow())  # Output: Meow!
