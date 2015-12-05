import unittest
from collatz_conjecture_measurer import apply_collatz_conjecture

class CollatzConjectureMeasurerTest(unittest.TestCase):
    def test_get_number_of_iterations_starting_on_1_should_return_0(self):
        n = apply_collatz_conjecture(1)
        self.assertIs(n == 0, True, "Iteration number was: " + str(n))

    def test_get_number_of_iterations_starting_on_2_should_return_1(self):
        n = apply_collatz_conjecture(2)
        self.assertIs(n == 1, True, "Iteration number was: " + str(n))

    def test_get_number_of_iterations_starting_on_3_should_return_7(self):
        n = apply_collatz_conjecture(3)
        self.assertIs(n == 7, True, "Iteration number was: " + str(n))

    def test_get_number_of_iterations_starting_on_4_should_return_2(self):
        n = apply_collatz_conjecture(4)
        self.assertIs(n == 2, True, "Iteration number was: " + str(n))

    def test_get_number_of_iterations_starting_on_0_should_raise_value_error_exception(self):
        with self.assertRaises(ValueError):
            n = apply_collatz_conjecture(0)

    def test_get_number_of_iterations_starting_on_negative_number_should_raise_value_error_exception(self):
        with self.assertRaises(ValueError):
            n = apply_collatz_conjecture(-1)
        
if __name__ == '__main__':
    unittest.main()