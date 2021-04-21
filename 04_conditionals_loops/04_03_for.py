'''
Using a "for-loop", print out all odd numbers from 1-100.

'''

start, end = 1, 100
for i in range(start, end):
    if i%2 == 0:
        continue
    else:
        print(i)
