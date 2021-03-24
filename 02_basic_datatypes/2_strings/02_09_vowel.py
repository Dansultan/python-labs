'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
sentence = input("Please enter a sentence: ")
i = 0
vowels = ['a','e','i','o','u','y']
for letter in sentence :
    if letter in vowels:
        i +=1
print ("The number of vowels is : ",i)


