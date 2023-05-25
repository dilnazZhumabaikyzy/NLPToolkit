import unittest
from data_processor import DataProcessor
from file_processors.csv_processor import CSVProcessor
from file_processors.html_processor import HTMLProcessor
from file_processors.xml_processor import XMLProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data_processor = DataProcessor()

    def test_load_file(self):
        # Create some sample files for testing
        folder_path = 'test_data'
        csv_file_path = 'test_data/sample.csv'
        html_file_path = 'test_data/sample.html'
        xml_file_path = 'test_data/sample.xml'

        # Register processors for different file extensions
        self.data_processor.register_processor('.csv', CSVProcessor())
        self.data_processor.register_processor('.html', HTMLProcessor())
        self.data_processor.register_processor('.xml', XMLProcessor())

        # Process the folder
        self.data_processor.load_file(folder_path)

        # Assert that the expected data is processed
        expected_data = {
            'test_file1.csv': 'this is my csv file for testing stage hello bts jungkook jin jimin yoongi taehyung hoseok thank you for attention',
            'test_file2.html': 'This is a test HTML file Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed euismod lacus eget sem placerat, vel iaculis magna consectetur.',
            'test_file3.xml': 'This is some sample text with symbols and numbers. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc aliquam, erat in iaculis sollicitudin, nisl nunc iaculis metus, in gravida orci massa in lorem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin ullamcorper lorem ut justo semper malesuada. Integer laoreet sagittis commodo. Maecenas ultrices dui non velit rhoncus commodo. Suspendisse vitae malesuada odio. 1234567890 ~'
        }
        self.assertDictEqual(self.data_processor.data, expected_data)

if __name__ == '__main__':
    unittest.main()
