from ..handler import Handler
from data_processor import DataProcessor

class FileLoadingHandler(Handler):
    def __init__(self):
        self.next_handler = None
        self.data_processor = DataProcessor()

    def set_next(self, handler):
        self.next_handler = handler
    
    def handle_request(self, request):
        if request == 'file_loading':
            # Load the file using your data_processor
            folder_path = "test_data"   # Specify the folder path to load files from
            self.data_processor.load_file(folder_path)
            print("File loading completed.")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("Invalid request.")
