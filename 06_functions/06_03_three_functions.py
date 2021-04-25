'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''


def multiply(n):
    y = n*n
    return y

def multiply_2(x):
    x = multiply(n)*2
    return x

def divide(z):
    w = multiply_2(x)/4
    return w


w=10
print(multiply())
