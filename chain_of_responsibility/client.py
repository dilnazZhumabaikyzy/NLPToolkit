from handler import Handler
from handlers.file_loading_handler import FileLoadingHandler
from handlers.preprocessing_handler import PreprocessingHandler

# Create the handlers
file_loading_handler = FileLoadingHandler()
preprocessing_handler = PreprocessingHandler()

# Chain the handlers
file_loading_handler.set_next(preprocessing_handler)

# Send requests
file_loading_handler.handle_request('file_loading')  # Process file loading
file_loading_handler.handle_request('preprocessing')  # Process preprocessing
