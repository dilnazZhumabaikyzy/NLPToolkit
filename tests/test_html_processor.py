import unittest
from file_processors.html_processor import HTMLProcessor

class TestHTMLProcessor(unittest.TestCase):
    def setUp(self):
        self.html_processor = HTMLProcessor()

    def test_process(self):
        # Test case 1: Provide a valid html file path
        file_path = 'test_data/test_file2.html'
        expected_result = 'This is a test HTML file Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod lacus eget sem placerat, vel iaculis magna consectetur.'

        processed_data = self.html_processor.process(file_path)
        # print(f"\nProcessed HTML file: {file_path}")  # Add this line for debugging
        self.assertEqual(processed_data, expected_result)

        # Test case 2: Provide an invalid file path
    def test_process_html_invalid_path(self):
        file_path = 'invalid/path/file.html'
        
        with self.assertRaises(FileNotFoundError):
            self.html_processor.process(file_path)
        
        # print(f"\nProcessed HTML file: {file_path}")



if __name__ == '__main__':
    unittest.main()
