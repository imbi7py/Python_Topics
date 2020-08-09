______ unittest

from phone_number ______ Phone


class PhoneTest(unittest.TestCase
    ___ test_cleans_number(self
        number = Phone("(123) 456-7890").number
        self.assertEqual(number, "1234567890")

    ___ test_cleans_number_with_dots(self
        number = Phone("123.456.7890").number
        self.assertEqual(number, "1234567890")

    ___ test_valid_when_11_digits_and_first_is_1(self
        number = Phone("11234567890").number
        self.assertEqual(number, "1234567890")

    ___ test_invalid_when_11_digits(self
        number = Phone("21234567890").number
        self.assertEqual(number, "0000000000")

    ___ test_invalid_when_9_digits(self
        number = Phone("123456789").number
        self.assertEqual(number, "0000000000")

    ___ test_area_code(self
        number = Phone("1234567890")
        self.assertEqual(number.area_code(), "123")

    ___ test_pretty_print(self
        number = Phone("1234567890")
        self.assertEqual(number.pretty(), "(123) 456-7890")

    ___ test_pretty_print_with_full_us_phone_number(self
        number = Phone("11234567890")
        self.assertEqual(number.pretty(), "(123) 456-7890")


__ __name__ __ '__main__':
    unittest.main()
