'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''

class Car:
    def __init__(self, model, year, max_speed=100):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def acceleration(self):
        self.max_speed += 5

    def __str__(self):
        return f'The model of this car is {self.model}, designed in {self.year} and with a maximum acceleration of {self.max_speed} km/h'

Dan_car = Car('Range Rover',2021 ,'350')
Martin_car = Car('Mercedes',2020,'320')

print(Dan_car)
print(Martin_car)