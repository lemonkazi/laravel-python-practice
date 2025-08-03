import unittest
from utilities.json_ops import fetch_json_data, save_json_to_file
import os
import json

class TestJsonOperations(unittest.TestCase):
    def test_fetch_json_data(self):
        url = "https://api.genderize.io?name=John"  # Example API for testing
        json_data = fetch_json_data(url)
        self.assertIsNotNone(json_data)
        self.assertIn("name", json_data)
        self.assertIn("gender", json_data)
        self.assertIn("probability", json_data)

    def test_fetch_json_data_invalid_url(self):
        url = "https://invalid-url.example.com"  # Invalid URL for testing
        json_data = fetch_json_data(url)
        self.assertIsNone(json_data)  # Expect None for invalid URL

    def test_save_json_to_file_invalid(self):
        data = {"name": "John", "gender": "male", "probability": 0.99}
        filename = "/invalid_path/test_result.json"  # Invalid path for testing
        with self.assertRaises(OSError):
            save_json_to_file(data, filename)

    def test_save_json_to_file(self):
        data = {"name": "John", "gender": "male", "probability": 0.99}
        filename = "test_result.json"
        save_json_to_file(data, filename)
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            saved_data = json.load(file)
            self.assertEqual(saved_data, data)
        os.remove(filename)  # Clean up the test file

if __name__ == '__main__':  # pragma: no cover
    unittest.main()
