# Homework 8_1
"""Catching incorrect symbols in the list of numbers.
"""


def catch_incorrect_symbols(lst):
    # separating all elements by comma
    for item in lst:
        item = item.split(',')

        try:
            result = [int(el) for el in item]

        except ValueError as e:
            print(f'Can`t do this, because ERROR is : {e}')

        else:
            print(sum(result))


catch_incorrect_symbols(['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3'])
