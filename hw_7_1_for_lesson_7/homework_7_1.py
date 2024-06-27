# Homework_7_1

# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
separator = "=================="


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result <= 25:
            # Enter the action to take if the result is greater than 25
            print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(5)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print(separator)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_of_two_numbers(a, b):
    return a + b


print(sum_of_two_numbers(2, 3))
print(separator)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average_of_list_numbers(values):
    return sum(values) / len(values)


print(int(average_of_list_numbers([1, 2, 3, 4, 5])))
print(separator)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def str_revers(val):
    return val[:: -1]


print(str_revers('Python is cool'))
print(separator)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longer_word_in_list(items):
    return max(items, key=len)


print(longer_word_in_list(['Endy', 'was', 'the', 'best', 'pupil']))
print(separator)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(first, second):
    if second in first:
        return first.find(second)
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1
print(separator)

# task 7
""" Sum of all even numbers in list.
"""


def sum_of_even_numbers(list_num):
    return f"Sum of all even numbers is: {sum(k for k in list_num if k % 2 == 0)}"


print(sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(separator)

# task 8
""" Creating new list with string values from another list.
"""


def values_in_another_list(values_list1):
    values_list_2 = [k for k in values_list1 if type(k) is str]
    return f"New list with string values: {values_list_2}"


print(values_in_another_list(['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']))
print(separator)

# task 9
""" Function which didn`t stop the cycle without word which include 'h' or 'H' letter.
"""


def word_with_h_letter(h_letter):
    my_str = input('Input your Word(Word must include "h" or "H" letter): ')
    while h_letter != "h" not in my_str.lower():
        my_str = input('Your Word has no "h" or "H". Please try again: ')
    return my_str


word_with_h_letter(h_letter=' ')
print(separator)

# task 10
""" list of tuples for functions.
"""
people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# task 10_1
"""  first function
Insert values for new person.
"""


def new_values_for_person(index, values):
    return people_records.insert(index, values)


new_values_for_person(0, ('Den', 'Neith', 25, 'Seller', 'Oklahoma'))
print(people_records)

# task 10_2
""" second function
Change indexes in list of tuples.
"""


def replace_indexes(ind1, ind2):
    people_records[ind1], people_records[ind2] = people_records[ind2], people_records[ind1]
    return ind1, ind2


replace_indexes(1, 5)
print(people_records)

# task 10_3
""" Third function 
Check that all people in modified list with records indexes 6, 10, 13
have age >=30. 
"""


def modified_list(first_i, second_i, third_i):
    first_person = people_records[first_i]
    second_person = people_records[second_i]
    third_person = people_records[third_i]
    new_list = [first_person, second_person, third_person]
    for person in new_list:
        if person[2] >= 30:
            print(False)
        else:
            print(True)
        return new_list


modified_list(6, 10, 13)

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
