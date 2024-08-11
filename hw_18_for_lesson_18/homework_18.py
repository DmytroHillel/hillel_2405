import logging

"""Декоратор логування у файл"""


def log_arguments_and_result_to_file(filename='my_log.txt'):
    logging.basicConfig(filename=filename, level=logging.INFO)

    def decorator(func):
        def wrapper(*args, **kwargs):
            logging.info(f"Calling {func.__name__} with arguments:")
            logging.info(f"Positional args: {args}")
            logging.info(f"Keyword args: {kwargs}")
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned: {result}")
            return result

        return wrapper

    return decorator


"""Декоратор перехоплення помилки"""


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except TypeError:
            print(f"'str' object cannot be interpreted as an integer")

    return wrapper


"""Декоратор перехоплення помилки(Денис)"""


def exception_decorator(generator_func):
    def wrapper(*args, **kwargs):
        try:
            generator = generator_func(*args, **kwargs)
            while True:
                try:
                    return generator
                except StopIteration:
                    break
                except Exception as e:
                    print(f"Caught an exception: {e}")
        except Exception as e:
            print(f"Failed to initialize generator: {e}")

    return wrapper


@exception_decorator
def faulty_generator(a, b):
    res = a / b
    print(res)


faulty_generator(5, 0)

"""Функція повернення послідовності парних чисел"""


@exception_decorator
def iven_number_generator(n):
    for num in range(n):
        if num % 2 == 0:
            yield num


for i in iven_number_generator(10):
    print(i)

print('=' * 50)
"""Функція генерування послідовності чисел Фібоначі"""


@handle_exceptions
def fibonacci_generator(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


fib = fibonacci_generator(300)
try:
    for i in range(20):
        print(next(fib))
except StopIteration:
    print('Stop iteration')

print('=' * 50)


class MyIterator:
    def __init__(self, min_num):
        self.min_num = min_num
        self.current = 100

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.min_num:
            self.current -= 1
            return self.current
        else:
            raise StopIteration


my_iterator = MyIterator(1)
for num in my_iterator:
    print(num)

print('=' * 50)


#
#
# iteration = iter(iven_number_generator(10))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))
# print(next(iteration))


@log_arguments_and_result_to_file()
class EvenNumber:
    def __init__(self, max_num):
        self.max_num = max_num
        self.min = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.min < self.max_num:
            self.min += 1
            return self.min
        else:
            raise StopIteration


even_numbers = EvenNumber(89)
for num in even_numbers:
    if num % 2 == 0:
        print(num)

print('=' * 50)
