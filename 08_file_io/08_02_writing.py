'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

fin = open('words.txt','r')

list = []

for word in fin.readlines():
    list.append(word)

new_list = []

for word in list:
    reversedstring=''.join(reversed(word))
    new_list.append(reversedstring)



print(new_list)

fout = open('words_reverse.txt','w')
fout.write(f'{new_list}')

    

