#docker-compose exec python python -m pytest my_basic_project/tests/
import unittest
from utilities.string_ops import capitalize_all

class TestStringOperations(unittest.TestCase):
    def test_capitalize_all(self):
        self.assertEqual(capitalize_all(["hello", "world", "python"]),
                         ["HELLO", "WORLD", "PYTHON"])
        self.assertEqual(capitalize_all([]), [])
        self.assertEqual(capitalize_all(["a"]), ["A"])

if __name__ == '__main__': # pragma: no cover
    unittest.main()
