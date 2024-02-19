"""
"""
"""
Benefits of Inheritance:
Code Reusability: Inheritance allows you to reuse code from existing classes, reducing redundancy and promoting code reuse.
Extensibility: Subclasses can extend the functionality of their superclass by adding new attributes and methods.
Maintainability: Inheritance helps in organizing code in a hierarchical manner, making it easier to understand and maintain.
Inheritance is a powerful mechanism in Python that enables code reuse and promotes modular design. It allows you to build complex systems by leveraging existing code and extending it as needed.
"""

class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return "Make some sound"


class Dog(Animal):
    def __init__(self, breed):
        # Call the constructor of the superclass (Animal)
        super().__init__("Canine")
        self.breed = breed

    # Function overriding
    def sound(self):
        return super().sound() + " Woof"


class Cat(Animal):
    def __init__(self, breed):
        # Call the constructor of the superclass (Animal)
        super().__init__("Feline")
        self.breed = breed

    # Function overriding
    def sound(self):
        return "Meow"


# Create instances of subclasses
dog = Dog("Labrador")
cat = Cat("Persian")

# Accessing attributes
print(dog.species)  # Output: Canine
print(dog.breed)  # Output: Labrador
print(dog.sound())  # Output: Woof
print(cat.species)  # Output: Feline
print(cat.breed)  # Output: Persian
