import unittest
from file_processors.xml_processor import XMLProcessor

class TestXMLProcessor(unittest.TestCase):
    def setUp(self):
        self.xml_processor = XMLProcessor()

    def test_process(self):
        file_path = 'test_data/test_file3.xml'
        expected_result = 'This is some sample text with symbols and numbers. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc aliquam, erat in iaculis sollicitudin, nisl nunc iaculis metus, in gravida orci massa in lorem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin ullamcorper lorem ut justo semper malesuada. Integer laoreet sagittis commodo. Maecenas ultrices dui non velit rhoncus commodo. Suspendisse vitae malesuada odio. 1234567890 ~'
        
        processed_data = self.xml_processor.process(file_path)
        # print(f"\nProcessed XML file: {file_path}")  # Add this line for debugging
        self.assertEqual(processed_data, expected_result)

    def test_process_xml_invalid_path(self):
        file_path = 'invalid/path/file.xml'
        
        with self.assertRaises(FileNotFoundError):
            self.xml_processor.process(file_path)
        
        # print(f"\nProcessed XML file: {file_path}")


if __name__ == '__main__':
    unittest.main()
