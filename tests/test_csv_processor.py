import unittest
from file_processors.csv_processor import CSVProcessor

class TestCSVProcessor(unittest.TestCase):
    def test_process(self):
        # Test case 1: Provide a valid CSV file path
        file_path = 'test_data/test_file1.csv'
        processor = CSVProcessor()
        processed_data = processor.process(file_path)
        expected_result = "this is my csv file for testing stage hello bts jungkook jin jimin yoongi taehyung hoseok thank you for attention"  # the expected result
        self.assertEqual(processed_data, expected_result)

        # Test case 2: Provide an invalid file path
        invalid_file_path = 'invalid/path/file.csv'
        with self.assertRaises(FileNotFoundError):
            processor.process(invalid_file_path)

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
