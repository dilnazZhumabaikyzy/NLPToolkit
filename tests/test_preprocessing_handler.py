import unittest
from chain_of_responsibility.handlers.preprocessing_handler import PreprocessingHandler
test_data = {
    'file1.txt': 'This is the content of file 1.',
    'file2.txt': 'Here is the content of file 2.',
    'file3.txt': 'And this is the content of file 3.'
}

class PreprocessingHandlerTest(unittest.TestCase):
    def test_handle_request_preprocessing(self):
        # Create the PreprocessingHandler instance with test data
        handler = PreprocessingHandler(test_data)

        # Mock any necessary dependencies or methods
        handler.adapter.preprocess = lambda: print("Mock preprocessing")

        # Send the preprocessing request
        handler.handle_request('preprocessing')

if __name__ == '__main__':
    unittest.main()

