from ..handler import Handler
from preprocess.adapters.preprocessing_adapter import PreprocessingAdapter

class PreprocessingHandler(Handler):
    def __init__(self, data):
        self.next_handler = None
        self.adapter = PreprocessingAdapter(data)  # Instantiate your PreprocessingAdapter here

    def set_next(self, handler):
        self.next_handler = handler
    
    def handle_request(self, request):
        if request == 'preprocessing':
            # Perform the preprocessing using your PreprocessingAdapter
            self.adapter.preprocess()
            print("Preprocessing completed.")
        elif self.next_handler:
            self.next_handler.handle_request(request)
        else:
            print("Invalid request.")
