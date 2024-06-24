# Homework 9_1

# 9_1_1
"""Sum function for int-type symbols and show incorrect symbols (not int) in the list of numbers.
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
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


# 9_1_5
"""Function of reversing the entry of another row into the first.
"""


def find_substring(first, second):
    if second in first:
        return first.find(second)
    else:
        return -1


