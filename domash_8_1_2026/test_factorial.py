import unittest
from .factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(factorial(5),120)

    def test_zero(self):
        self.assertEqual(factorial(0),1)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_not_integer(self):
        with self.assertRaises(ValueError):
            factorial(2.5)


if __name__ == '__main__ ':
    unittest.main()
