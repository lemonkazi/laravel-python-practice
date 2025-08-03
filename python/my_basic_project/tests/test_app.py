import unittest
from unittest.mock import patch
from io import StringIO
import app

class TestApp(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        app.main()
        output = mock_stdout.getvalue()

        expected_outputs = [
            "Addition of 5 and 3: 8",
            "Multiplication of 4 and 2: 8",
            "Subtraction of 10 and 6: 4",
            "Division of 8 by 2: 4.0",
            "Cannot divide by zero",
            "Capitalized words: ['HELLO', 'WORLD', 'PYTHON']"
        ]

        for expected in expected_outputs:
            self.assertIn(expected, output)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
