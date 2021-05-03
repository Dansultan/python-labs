'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet:
    def __init__(self,name,diameter,distance_from_earth,color):
        self.name = name
        self.diameter = diameter
        self.distance_from_earth = distance_from_earth
        self.color = color

    def __str__(self):
        return f"The planet {self.name} has a diameter {self.diameter} at a distance of {self.distance_from_earth} km from the earth. It's color is {self.color}."

mars = Planet('Mars','12 Thousands km','334 Thousands','Red')

print(mars)