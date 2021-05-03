'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets at least three attributes
- Include a __str__ method in each class that prints out the attributes
    in a nicely formatted string.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Create at least two instances of each class.
- Once the objects are created, change some of their attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, card games, sports teams, trees, people etc...

'''

class Sports_team:
    def __init__(self,name,city,best_player):
        self.name = name
        self.city = city
        self.best_player = best_player

    def __str__(self):
        return f"This team is the {self.name} ! They represent the city of {self.city} and their best player is {self.best_player}"

class Shoes:
    def __init__(self,brand,model,color,):
        self.brand = brand
        self.model = model
        self.color = color


    def __str__(self):
        return f"This pair from {self.brand}, and the name of this model is {self.model}. They look great in this {self.color} color !"

class Money:
    def __init__(self,at_home,in_the_bank):
        self.at_home = at_home
        self.in_the_bank = in_the_bank

    def __add__(self, other):
        total = self.at_home + self.in_the_bank
        return Money('The total of money that I have is :',total)


my_favorite = Shoes ('Nike','Cortez','Black')
print(my_favorite)

my_gain = Money(1000,3400)
print(my_gain)






