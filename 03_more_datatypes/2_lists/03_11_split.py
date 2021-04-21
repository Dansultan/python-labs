'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
sentence = input("Please write :")
list = sentence.split()


def most_frequent(List):
    counter = 0
    num = list[0]

    for i in list:
        curr_frequency = list.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i

    return num

word = most_frequent(list)

print("The word with the most occurrences is:",word)

