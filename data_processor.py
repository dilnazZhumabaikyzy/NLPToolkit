import os
import json


class DataProcessor:
    def __init__(self):
        self.file_processors = {}
        self.data = {}

    def register_processor(self, file_extension, processor):
        self.file_processors[file_extension] = processor

    def process_folder(self, folder_path):
        data = {}  # Initialize an empty dictionary to store file data
        def get_file_extension(file_name):
                    _, file_extension = os.path.splitext(file_name)
                    return file_extension
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                file_extension = get_file_extension(file_name)
                processor = self.file_processors.get(file_extension)
                if processor:
                    print(f"Processing {file_extension.upper()} file: {file_path}")
                    content = processor.process(file_path)
                    data[file_name] = content
                else:
                    print(f"No processor found for file: {file_name}")

        # Convert data dictionary to JSON format
        # json_data = json.dumps(data)
        self.data = data
        # Do something with the JSON data (e.g., save it to a file or return it)

