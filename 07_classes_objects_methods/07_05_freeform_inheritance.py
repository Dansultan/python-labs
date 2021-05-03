'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Sports_team:
    def __init__(self,name,city,best_player):
        self.name = name
        self.city = city
        self.best_player = best_player

    def __str__(self):
        return f"This team is the {self.name} ! They represent the city of {self.city} and their best player is {self.best_player}"

class Shoes:
    def __init__(self,brand,model,color):
        self.brand = brand
        self.model = model
        self.color = color


    def __str__(self):
        return f"This pair from {self.brand}, and the name of this model is {self.model}. They look great in this {self.color} color !"


class Vintage(Shoes):

    def __init__(self,brand,model,color,year):
        super().__init__(brand,model,color)
        self.year = year

    def __str__(self):
        return f"Wooow, this {self.model} is from {self.year} ! One of the best model of {self.brand}, particulary in this {self.color} color!"


class Money:
    def __init__(self,at_home,in_the_bank):
        self.at_home = at_home
        self.in_the_bank = in_the_bank

    def __add__(self, other):
        total = self.at_home + self.in_the_bank
        return Money('The total of money that I have is :',total)


my_shoes = Vintage('Nike','Cortez','Black','1985')
print(my_shoes)

