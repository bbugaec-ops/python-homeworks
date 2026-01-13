import unittest
from domash_8_1_2026.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(a=2,b= 3), 5)
        self.assertEqual(self.calc.add(a=-1,b= 1), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(1, 10), -9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

    def test_maximum(self):
        self.assertEqual(self.calc.maximum(10, 20), 20)
        self.assertEqual(self.calc.maximum(5, 5), 5)

    def test_minimum(self):
        self.assertEqual(self.calc.minimum(10, 20), 10)
        self.assertEqual(self.calc.minimum(5, 5), 5)

    def test_percent(self):
        self.assertEqual(self.calc.percent(200, 10), 20)
        self.assertEqual(self.calc.percent(50, 50), 25)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)


if __name__ == "__main__":
    unittest.main()
