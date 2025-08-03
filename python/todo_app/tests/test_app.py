import unittest
from unittest.mock import patch
from io import StringIO
import app

class TestApp(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_output(self, mock_stdout):
        with patch('builtins.input', side_effect=['5', '1', '2', 'Test Task', '3', '1', '4']):
            app.main()
        output = mock_stdout.getvalue()

        # Verify invalid choice handling
        self.assertIn("⚠️ Invalid choice. Try again.", output)

        # Verify menu options appear
        self.assertIn("1. View tasks", output)
        self.assertIn("3. Mark task as done", output)
        self.assertIn("4. Exit", output)

        # Verify task addition flow
        self.assertIn("✅ Task added.", output)

        # Verify task completion flow
        self.assertIn("✅ Task marked as completed.", output)

        # Verify exit saving
        self.assertIn("📝 Tasks saved. Goodbye!", output)


if __name__ == '__main__': # pragma: no cover
    unittest.main()
