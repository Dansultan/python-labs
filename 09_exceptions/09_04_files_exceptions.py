'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

with open('books/war_and_peace.txt','r') as first_text:
    data_1 = first_text.read()

with open('books/crime_and_punishment copy.txt','r') as second_text:
    data_2 = second_text.read()

with open('books/pride_and_prejudice.txt','r') as third_text:
    data_3 = third_text.read()

list_1 = []
for words in data_1:
    list_1.append(words)


list_2 = []
for words in data_2:
    list_2.append(words)

list_3 = []
for words in data_3:
    list_3.append(words)

print(list_1[0])
print(list_2[0])
print(list_3[0])

fin_2 = open('books/crime_and_punishment.txt','r+')
text_2 = fin_2.read()
fin_2.seek(0)
fin_2.write('')
fin_2.truncate()

