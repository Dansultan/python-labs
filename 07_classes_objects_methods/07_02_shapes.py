'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
import math


class Rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width

    def area(self):
        x = self.lenght*self.width
        print(f'The area of the rectangle is {x} cm^2')

class Circle:
    def __init__(self,radius):
        self.radius = radius


    def circumference(self):
        y = self.radius*2*math.pi
        print(f'The circumference of the circle is {y} cm^3ֵ')


first_rectangle = Rectangle(7,2)
first_rectangle.area()
print(first_rectangle)

second_circle = Circle(3)
second_circle.circumference()
print(second_circle)






