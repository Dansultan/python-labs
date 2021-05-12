'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
import pdb; pdb.set_trace()

fin = open('words.txt','r')
list = []


for word in fin.readlines():
    list.append(word)

longest_string = max(list,key=len)
smallest_string = min(list,key=len)
separate_words = len(list)


print('The longest string is:',longest_string)
print('The smallest string is:',smallest_string)
print('The number of words is :',separate_words)

fin.close()





