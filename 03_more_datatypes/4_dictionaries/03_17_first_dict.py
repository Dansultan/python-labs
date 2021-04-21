'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''

item1=0

item2 = item1*item1
user = {item1: item2}

for x,y in user.items():
    if item1<=0:
       item1+=1
       user[item1]=item2
    else:
        break


print(user)