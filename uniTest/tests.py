import unittest
from uniTest.main import add, devide

class My_test_for_add(unittest.TestCase):
    def test_args(self):
        self.assertEqual(add(2, 2),4)

    def test_kwargs(self):
        self.assertEqual(add(a=2, b=4),6)

    def test_mixed(self):
        self.assertEqual(add(1, a=2, b=4),7)

    def test_diff(self):
        x = 10
        y = 0
        self.assertEqual(add(0,-5,y,a=x),5)

    def test_wrong_datatype(self):
        self.assertEqual(add("5","qwerty",10),15)


class My_test_for_devide(unittest.TestCase):
    def test_args(self):
        self.assertEqual(devide(2, 2),4)

    def test_kwargs(self):
        self.assertEqual(devide(a=2, b=4),6)

    def test_mixed(self):
        self.assertEqual(devide(1, a=2, b=4),7)




if  __name__ == "__main__":
    unittest.main()




