'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''

my_list = ["Bonjour","je","m'appelle","Dan"]

try:
    print(my_list[4])
except IndexError:
    print("Sorry, we can't help you")


