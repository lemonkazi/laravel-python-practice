import json
from unittest.mock import patch
import os
from io import StringIO
import unittest
from utilities.todo_ops import load_tasks, save_tasks, add_task, list_tasks, complete_task

# Test data
TEST_FILE = "todo_app/todo.json"

class TestTodoOperations(unittest.TestCase):
    # def setUp(self):
    #     # Setup: Create a test file
    #     with open(TEST_FILE, "w") as f:
    #         json.dump([{"title": "Test Task", "done": False}], f)
    #     yield
    #     # Teardown: Remove the test file
    #     os.remove(TEST_FILE)

    def test_load_tasks(self):
        tasks = load_tasks()
        assert len(tasks) == 1
        assert tasks[0]["title"] == "Test Task"

    def test_save_tasks(self):
        tasks = [{"title": "Test Task", "done": False}]
        save_tasks(tasks)
        with open(TEST_FILE, "r") as f:
            saved_tasks = json.load(f)
        assert len(saved_tasks) == 1
        assert saved_tasks[0]["title"] == "Test Task"

    @patch('builtins.input', side_effect=['Test Task'])
    def test_add_task(self, mock_input):
        tasks = []
        add_task(tasks)
        assert len(tasks) == 1
        assert tasks[0]["title"] != ""

    def test_list_tasks_empty(self):
        tasks = []
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            list_tasks(tasks)
        output = mock_stdout.getvalue()
        assert "📭 No tasks yet." in output

    def test_add_task_empty_title(self):
        tasks = []
        with patch('builtins.input', side_effect=['']):
            add_task(tasks)
        assert len(tasks) == 0

    def test_complete_task_valid_number(self):
        tasks = load_tasks()
        with patch('builtins.input', side_effect=['1']):
            complete_task(tasks)
        assert tasks[0]["done"] is True
        tasks = load_tasks()
        with patch('builtins.input', side_effect=['2']):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                complete_task(tasks)
        output = mock_stdout.getvalue()
        assert "⚠️ Invalid task number." in output
        tasks = load_tasks()
        with patch('builtins.input', side_effect=['1']):
            complete_task(tasks)
        assert tasks[0]["done"] is True

    def test_load_tasks_missing_file(self):
        # Remove the test file to test missing file case
        os.remove(TEST_FILE)
        tasks = load_tasks()
        self.assertEqual(len(tasks), 0)

    def test_save_tasks_none(self):
        save_tasks(None)
        with open(TEST_FILE, "r") as f:
            saved_tasks = json.load(f)
        self.assertEqual(len(saved_tasks), 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_complete_task_invalid_input(self, mock_stdout):
        tasks = load_tasks()
        with patch('builtins.input', side_effect=['invalid']):
            complete_task(tasks)
        output = mock_stdout.getvalue()
        self.assertIn("⚠️ Enter a valid number.", output)

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
