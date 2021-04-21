'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
first_number = int(input("Please enter your first number :"))
second_number = int(input("Please enter your second number :"))
third_number = int(input("Please enter your third number :"))
forth_number = int(input("Please enter your forth number :"))
fifth_number = int(input("Please enter your fifth number :"))
sixth_number = int(input("Please enter your sixth number :"))
seventh_number = int(input("Please enter your seventh number :"))
eighth_number = int(input("Please enter your eighth number :"))
ninth_number = int(input("Please enter your ninth number :"))
tenth_number = int(input("Please enter your tenth number :"))

list = [first_number,second_number,third_number,forth_number,fifth_number,sixth_number,seventh_number,eighth_number,ninth_number,tenth_number]

a = max(list)
print("The biggest number is :",a)