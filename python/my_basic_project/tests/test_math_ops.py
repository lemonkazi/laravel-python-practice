import unittest
from utilities.math_ops import add, multiply, subtract, divide

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)

    def test_multiply(self):
        self.assertEqual(multiply(4, 2), 8)
        self.assertEqual(multiply(3, 0), 0)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(1, 999), 999)
        self.assertAlmostEqual(multiply(2.5, 4), 10.0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 6), 4)
        self.assertEqual(subtract(5, -3), 8)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, -5), 3)
        self.assertAlmostEqual(subtract(5.5, 2.3), 3.2)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4.0)
        self.assertEqual(divide(8, 0), "Cannot divide by zero")
        self.assertEqual(divide(0, 5), 0.0)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(10, -2), -5.0)
        self.assertAlmostEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(100, 0), "Cannot divide by zero")

if __name__ == '__main__': # pragma: no cover
    unittest.main()
