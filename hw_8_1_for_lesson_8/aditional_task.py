class FormulaError(Exception):
    def init(self, text):
        self.text = text


class WrongOperatorError(Exception):
    def init(self, text):
        self.txt = text


counter = 3
while counter != 0:
    try:
        a, b, c = input('Enter the value separated by a space(format: (example: 1 * 1)): ').split(' ')
        a = int(a)
        b = str(b)
        c = int(c)
        if b == '*':
            res = a * c
            print(res)
            continue
        elif b == '/':
            res = a / c
            print(res)
            continue
    except ZeroDivisionError:
        print('Can`t divide by zero!')
    except (ValueError, NameError, FormulaError):
        print('Must be 3 values in format(int str int)')
    else:
        WrongOperatorError
        print(f'Operator must be "*" or "/"')
    counter = counter - 1
    print(f'{counter} left')
else:
    print('Finish')
