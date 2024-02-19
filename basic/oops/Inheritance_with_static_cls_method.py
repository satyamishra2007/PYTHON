"""
"""

"""
Certainly! Let's add static and class methods to the example to demonstrate their usage along with overriding methods:

"""


class Animal:
    @staticmethod
    def make_sound(sound):
        return f"Make {sound} sound"

    @classmethod
    def class_method(cls):
        return f"This is a class method of {cls.__name__}"

    def instance_method(self):
        return "This is an instance method"


class Dog(Animal):
    def sound(self):
        # Call the parent class method using super()
        return super().make_sound("Woof")


class Cat(Animal):
    def sound(self):
        # Call the parent class method using super()
        return super().make_sound("Meow")


# Create instances of subclasses
dog = Dog()
cat = Cat()

# Call the overridden method
print(dog.sound())  # Output: Make Woof sound
print(cat.sound())  # Output: Make Meow sound

# Call class and static methods
print(Dog.class_method())  # Output: This is a class method of Dog
print(Dog.make_sound("Bark"))  # Output: Make Bark sound
