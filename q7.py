class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def describe_car(self):
        print("")

Comment on Task 1:

This function below helps to create a Car class.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")


A class is like a blueprint for creating objects

Here, the object is a car
Each car should have:
make like Toyota
model like Corolla
year like 2020
The __init__ method is used to give these values when a car object is created.

The describe_car() method shows the car details in this format:

Year Make Model


Coding Example:

car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()
Output:

2020 Toyota Corolla


This task is about making a car class that stores car details and prints them nicely.

-------------------------------------------------------------------------------------------------


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020


Comments on Task 2:

Task 2 is to create one car object using the Car class, then use the method to show its details.

The function code is:

car1 = Car("Toyota", "Corolla", 2020)
car1.describe_car()

It means:

car1 = Car("Toyota", "Corolla", 2020) creates a car object
"Toyota" is the make
"Corolla" is the model
2020 is the year

And:

car1.describe_car() prints the car information
Output: 
2020 Toyota Corolla

Task 2 is just creating one car and displaying its details.
