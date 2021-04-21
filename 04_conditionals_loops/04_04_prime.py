'''
Print out every prime number between 1 and 100.

'''

start, end = 1, 100
for i in range(start, end):
    if i%2 ==0:
        continue
    elif i == 3 or i == 5:
        print(i)
    elif i%3 ==0:
        continue
    elif i%5 == 0:
        continue
    else:
        print(i)