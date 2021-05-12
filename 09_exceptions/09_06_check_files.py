'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
fin = open('integers.txt','r')

new_list = []

for number in fin:
    new_list.append(number)
try:
    calculation = int(new_list[0])/2
except ValueError:
    print('We need a number')
except IOError:
    print("We can't find the number !")
else:
    print(calculation)




