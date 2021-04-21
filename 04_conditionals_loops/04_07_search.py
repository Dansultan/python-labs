'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''

number = int(input("Please choose a number between 1 and 1,000,000 : "))

i = 0

while i <= 1000000:
    i+=1
    if i == number:
        print(i)
    else:
        continue

