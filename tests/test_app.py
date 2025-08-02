import unittest
from unittest.mock import patch
from io import StringIO
from python.my_basic_project.app import main

class TestApp(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        expected_output = (
            "Addition of 5 and 3: 8\n"
            "Multiplication of 4 and 2: 8\n"
            "Subtraction of 10 and 6: 4\n"
            "Division of 8 by 2: 4.0\n"
            "Division by zero test: Cannot divide by zero\n"
            "Capitalized words: ['HELLO', 'WORLD', 'PYTHON']\n"
        )
        
        main()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
