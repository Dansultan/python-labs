'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

fin = open('words.txt','r')


list = []
for word in fin.readlines():
    if len(word) >=20:
        list.append(word)
    else:
        pass

print(list)

