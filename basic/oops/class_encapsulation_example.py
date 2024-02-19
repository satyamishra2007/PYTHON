"""
"""

"""
Encapsulation is one of the fundamental principles of object-oriented programming (OOP). 
It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit (class). 
Encapsulation hides the internal state of an object from the outside world and only exposes a controlled interface for interacting with the object. 
Let's illustrate encapsulation in Python with an example:
"""


class Car:
    def __init__(self, make, model, year):
        self._make = make  # Protected attribute
        self._model = model  # Protected attribute
        self._year = year  # Protected attribute
        self._odometer_reading = 0  # Protected attribute, initialized to 0

    # Getter method for odometer_reading
    def get_odometer_reading(self):
        return self._odometer_reading

    # Setter method for odometer_reading
    def set_odometer_reading(self, mileage):
        if mileage >= self._odometer_reading:
            self._odometer_reading = mileage
        else:
            print("Odometer reading cannot be rolled back!")

    # Method to increment odometer_reading
    def increment_odometer(self, miles):
        if miles >= 0:
            self._odometer_reading += miles
        else:
            print("Invalid mileage value!")


# Create an instance of Car
my_car = Car("Toyota", "Corolla", 2022)

# Accessing protected attributes directly (not recommended)
print(my_car._make)  # Output: Toyota

# Accessing encapsulated attribute using getter method
print(my_car.get_odometer_reading())  # Output: 0

# Updating encapsulated attribute using setter method
my_car.set_odometer_reading(100)
print(my_car.get_odometer_reading())  # Output: 100

# Incrementing encapsulated attribute using method
my_car.increment_odometer(50)
print(my_car.get_odometer_reading())  # Output: 150

# Trying to roll back odometer_reading (should not be allowed)
my_car.set_odometer_reading(100)
print(my_car.get_odometer_reading())  # Output: 150 (not rolled back)

"""

In this example:
We define a Car class with attributes _make, _model, _year, and _odometer_reading. These attributes are prefixed with an underscore _ to indicate that they are protected, meaning they should not be accessed directly from outside the class.
We provide getter and setter methods (get_odometer_reading() and set_odometer_reading()) to access and modify the _odometer_reading attribute, respectively. This encapsulates the attribute and provides controlled access to it.
We also provide a method (increment_odometer()) to increment the _odometer_reading attribute by a specified number of miles.
When creating an instance of Car (my_car), we interact with the encapsulated attributes using getter, setter, and method calls, rather than accessing them directly.

Encapsulation helps in hiding the internal implementation details of 
a class and provides a clean and controlled interface 
for interacting with objects. It enhances data security, prevents accidental modification 
of internal state, and promotes modular and maintainable code.

"""
