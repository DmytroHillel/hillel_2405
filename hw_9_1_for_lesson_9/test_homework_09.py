from homeworks import *
import unittest


class TestFunctions(unittest.TestCase):

    # funktion 9_1_1
    def test_string_incorrect_values(self):
        int_with_str = revision_of_string_values(['1,2,3,4', '1,2,3,4,50', 'que1,2,3'])
        self.assertFalse(int_with_str)

    def test_string_correct_values(self):
        int_without_str = revision_of_string_values(['1,2,3,4', '1,2,3,4,50', '1,2,3'])
        self.assertTrue(int_without_str)

    def test_string_with_int(self):
        with self.assertRaises(AttributeError):
            only_int = revision_of_string_values([1, 2, 3, 4])
            self.assertEqual(only_int, "'int' object has no attribute 'split'")

    # funktion 9_1_2
    def test_average_with_correct_values(self):
        inputted_val = [1, 2, 3, 4, 5]
        actual_result = 3
        self.assertEqual(average_of_list_numbers(inputted_val), actual_result)

    def test_average_with_unexpected_value(self):
        default_values = average_of_list_numbers([1, 2, 3, 4, 5])
        self.assertEqual(default_values, 2, msg=f"expected result is 2, but actual is{default_values}")

    def test_average_without_values(self):
        with self.assertRaises(ZeroDivisionError):
            res = average_of_list_numbers([])
            self.assertEqual(res, "division by zero")

    # def test_str_values(self):
    #     with self.assertRaises(TypeError):
    #         average_of_list_numbers(['1,2,3,4'])

    def test_average_with_str_values(self):
        with self.assertRaises(TypeError) as error:
            inputted_val = average_of_list_numbers('Potter')
            result = error.exception.args[inputted_val]
            self.assertEqual(result, "unsupported operand type(s) for +: 'int' and 'str'")

    # funktion 9_1_3
    def test_with_even_numbers(self):
        list_with_even_numbers = sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(list_with_even_numbers, 30)

    def test_without_even_numbers(self):
        list_without_even_numbers = sum_of_even_numbers([1, 3, 5, 7, 9])
        self.assertEqual(list_without_even_numbers, 0)

    # def test_even_numbers(self):
    #     result = sum_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #     self.assertTrue(result)

    # funktion 9_1_4
    def test_mult_table_correct_val(self):
        int_num = multiplication_table(5)
        self.assertTrue(int_num)

    def test_mult_table_str_val(self):
        with self.assertRaises(TypeError) as error:
            negative_num = multiplication_table('asd')
            res = error.exception.args[negative_num]
            self.assertFalse(res, "'<=' not supported between instances of 'int' and 'str'")

    def test_mult_table_zero_val(self):
        zero_val = multiplication_table(0)
        self.assertFalse(zero_val)

    # funktion 9_1_5
    def test_entry_second_in_first(self):
        values = find_substring("Hello World", "World")
        self.assertEqual(values, 6)

    def test_incorrect_second(self):
        values = find_substring("Hello World", "Word")
        self.assertEqual(values, -1)

    def test_int_val_for_second(self):
        with self.assertRaises(TypeError) as error:
            values = find_substring('1,2,3', 1)
            result = error.exception.args[values]
            self.assertEqual(result, "in <string> requires string as left operand, not int")


if __name__ == '__main__':
    unittest.main()

