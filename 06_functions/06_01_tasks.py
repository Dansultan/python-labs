'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results

def func_1(n):
    if n%4 == 0 or n%7 == 0:
        return True
    else:
        return False

def func_2(n):
    if n%4==0 and n%7==0:
        return True
    else:
        return False

number = int(input("Please enter a number from 1 to 1,000,000 :"))

print(func_1(number))
print(func_2(number))