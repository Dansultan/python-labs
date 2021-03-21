'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

#float(int)
#int (float)

x = 50.0
y = 25
divison = x/y
print (divison)

first = int(input("Please enter the first number to multiplicate :"))
second = int(input("Please enter the second number to multiplicate :"))
result = first*second
print (result)