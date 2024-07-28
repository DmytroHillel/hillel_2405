
# def iven_number_generator(n):
#     for num in range(n):
#         if num % 2 == 0:
#             yield num
#
#
# for i in iven_number_generator(10):
#     print(i)
#
#
# def fibonacci_generator(n):
#     a, b = 0, 1
#     while a < n:
#         yield a
#         a, b = b, a + b
#
#
# fib = fibonacci_generator(300)
# try:
#     for i in range(20):
#         print(next(fib))
# except StopIteration:
#     print('Stop iteration')


# class MyIterator:
#     def __init__(self, min_num):
#         self.min_num = min_num
#         self.current = 100
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current > self.min_num:
#             self.current -= 1
#             return self.current
#         else:
#             raise StopIteration
#
#
# my_iterator = MyIterator(1)
# for num in my_iterator:
#     print(num)


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