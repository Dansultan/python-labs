'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''

start, end = 1, 1000
i = 0
while i <= 1000:
    i+=1
    if i%5 == 0:
        print(i)
    else:
        continue
