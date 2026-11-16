# https://github.com/HoangKhoi1234/lab11-MHK-JZ
# Partner 1: Mai Hoang Khoi
# Partner 2: Jessica Zhang
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 5), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-4, 5), -20)
        self.assertEqual(multiply(0, 9), 0)

    def test_divide(self): # 3 assertions
        # divide(a, b) returns b / a
        self.assertEqual(divide(2, 10), 5)
        self.assertAlmostEqual(divide(4, 2), 0.5)
        self.assertEqual(divide(-5, 10), -2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument
        with self.assertRaises(ValueError):
            square_root(-1)
        # Test basic function
        self.assertAlmostEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=6)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
