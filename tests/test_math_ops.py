import unittest
from python.my_basic_project.utilities.math_ops import add, multiply, subtract, divide

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(2.5, 3.5), 6.0)

    def test_multiply(self):
        self.assertEqual(multiply(4, 2), 8)
        self.assertEqual(multiply(-3, 3), -9)
        self.assertEqual(multiply(2.5, 4), 10.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 6), 4)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(3.5, 1.5), 2.0)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)
        self.assertEqual(divide(9, 4), 2.25)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(8, 0), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
