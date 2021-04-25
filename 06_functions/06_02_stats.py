'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(n):
  print("The maximum of the list is :",max(example_list))
  print("The minimum of the list is :",min(example_list))
  print("The sum of the elements in the list is :",sum(example_list))
  long = len(example_list)
  average = sum(example_list)/long
  print("The average of the elements in the list is :",average)
  pass

print(stats(example_list))