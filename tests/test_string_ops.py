import unittest
from python.my_basic_project.utilities.string_ops import capitalize_all

class TestStringOperations(unittest.TestCase):
    def test_capitalize_all(self):
        self.assertEqual(
            capitalize_all(["hello", "world", "python"]),
            ["HELLO", "WORLD", "PYTHON"]
        )
        self.assertEqual(
            capitalize_all(["mixED", "CaSes", "TEST"]),
            ["MIXED", "CASES", "TEST"]
        )
        self.assertEqual(capitalize_all([]), [])

if __name__ == '__main__':
    unittest.main()
