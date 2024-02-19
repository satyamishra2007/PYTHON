"""
"""

"""

Polymorphism is a core concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. 
It enables the same interface (method name) to be used for different types of objects, promoting code reuse and flexibility. 
Let's demonstrate polymorphism in Python with an example:

In this example:

We have a superclass Animal with a method speak(), which is marked as abstract by raising a NotImplementedError.
We have three subclasses Dog, Cat, and Bird, each of which implements the speak() method with its own behavior.
We have a function make_sound() that takes an Animal object as an argument and calls its speak() method.
We create instances of different subclasses (dog, cat, bird) and pass them to the make_sound() function.
Despite the different types of objects being passed to make_sound(), the function works correctly, demonstrating polymorphism. It treats all objects as instances of the common superclass Animal and calls the appropriate speak() method for each object type.
Polymorphism allows us to write more flexible and reusable code. We can define functions and methods to operate on objects of a common superclass without needing to know the specific subclass types. This promotes loose coupling and makes our code more adaptable to changes and extensions in the future.
"""


class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement speak method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Bird(Animal):
    def speak(self):
        return "Tweet!"


# Function demonstrating polymorphism
def make_sound(animal):
    return animal.speak()


# Create instances of different classes
dog = Dog()
cat = Cat()
bird = Bird()

# Call the function with different types of objects
print(make_sound(dog))  # Output: Woof!
print(make_sound(cat))  # Output: Meow!
print(make_sound(bird))  # Output: Tweet!
