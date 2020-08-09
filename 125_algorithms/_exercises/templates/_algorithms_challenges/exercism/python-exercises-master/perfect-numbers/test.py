______ unittest

from perfect_numbers ______ is_perfect


class PerfectNumbersTest(unittest.TestCase

    ___ test_first_perfect_number(self
        self.assertTrue(is_perfect(6))

    ___ test_no_perfect_number(self
        self.assertFalse(is_perfect(8))

    ___ test_second_perfect_number(self
        self.assertTrue(is_perfect(28))

    ___ test_abundant(self
        self.assertFalse(is_perfect(20))

    ___ test_answer_to_the_ultimate_question_of_life(self
        self.assertFalse(is_perfect(42))

    ___ test_third_perfect_number(self
        self.assertTrue(is_perfect(496))

    ___ test_odd_abundant(self
        self.assertFalse(is_perfect(945))

    ___ test_fourth_perfect_number(self
        self.assertTrue(is_perfect(8128))

    ___ test_fifth_perfect_number(self
        self.assertTrue(is_perfect(33550336))

    ___ test_sixth_perfect_number(self
        self.assertTrue(is_perfect(8589869056))

    ___ test_seventh_perfect_number(self
        self.assertTrue(is_perfect(137438691328))


__ __name__ __ '__main__':
    unittest.main()
