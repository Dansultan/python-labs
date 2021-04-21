'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

def get_unique_numbers(list_):
    unique_list = []

    for number in list_:
        if number in unique_list:
            unique_list.remove(number)
        else:
            unique_list.append(number)
    return unique_list


print(get_unique_numbers(list_))