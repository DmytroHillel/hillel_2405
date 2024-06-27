# Homework 9_1

# 9_1_1
"""Sum function for int-type symbols and show incorrect symbols (not int) in the list of numbers.
"""
from typing import Any


def revision_of_string_values(lst):
    # separating all elements by comma
    for item in lst:
        try:
            item = item.split(',')
            result = [int(el) for el in item]
            print(sum(result))
        except ValueError as e:
            print(f'Can`t do this, because ERROR is : {e}')
            return False
    return result


# 9_1_2
"""Function for calculating the arithmetic mean of a list of numbers.
"""


def average_of_list_numbers(values):
    return int(sum(values) / len(values))


# # 9_1_3
"""Sum of all even numbers in list.
"""


def sum_of_even_numbers(list_num):
    return sum(k for k in list_num if k % 2 == 0)


# # 9_1_4
"""Print function up to the specified maximum value of the number.
"""


def multiplication_table(number):

    multiplier = 1

    while multiplier <= number:
        res = number * multiplier
        multiplier += 1
        if number <= 0:
            return False
        else:
            return res


# 9_1_5
"""Function of reversing the entry of another row into the first.
"""


def find_substring(first, second):
    return first.find(second)


# str_1 = 'Hello World'
# str_2 = 'Word'
# print(find_substring(str_1, str_2))
