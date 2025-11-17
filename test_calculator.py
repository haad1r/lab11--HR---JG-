# https://github.com/haad1r/lab11--HR---JG-
# Partner 1: Haadi Rattansi
# Partner 2: Juan Garcia

import unittest
from calculator import *
import math


class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(5, 5), 10)

    def test_subtract(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(5, 10), -5)

    # Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):
        self.assertEqual(div(25, 100), 4)
        self.assertEqual(div(6, 3), 0.5)
        self.assertEqual(div(-1, 5), -5)

    # Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)

    def test_logarithm(self):
        self.assertEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(10, 100), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(-2, 8)

    # Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(1.5, 2.0), math.hypot(1.5, 2.0))
        self.assertEqual(hypotenuse(0, 5), 5)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
