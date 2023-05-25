import unittest
from chain_of_responsibility.handlers.file_loading_handler import FileLoadingHandler
from chain_of_responsibility.handlers.preprocessing_handler import PreprocessingHandler

class ChainOfResponsibilityTest(unittest.TestCase):
    def test_chain_of_responsibility(self):
        # Create the handlers
        file_loading_handler = FileLoadingHandler()
        preprocessing_handler = PreprocessingHandler(file_loading_handler.data_processor.data)

        # Set the next handler in the chain
        file_loading_handler.set_next(preprocessing_handler)

        # Send requests through the chain
        file_loading_handler.handle_request('file_loading')
        file_loading_handler.handle_request('preprocessing')
        file_loading_handler.handle_request('invalid_request')

if __name__ == '__main__':
    unittest.main()
