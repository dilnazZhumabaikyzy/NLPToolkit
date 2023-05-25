import unittest
from chain_of_responsibility.handlers.file_loading_handler import FileLoadingHandler

class FileLoadingHandlerTest(unittest.TestCase):
    def test_handle_request_file_loading(self):
        handler = FileLoadingHandler()
        # Mock the data_processor's load_file method
        handler.data_processor.load_file = lambda folder_path: print("Mock file loading")
        # Send file_loading request
        handler.handle_request('file_loading')

if __name__ == '__main__':
    unittest.main()
