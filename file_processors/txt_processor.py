from .file_processor import FileProcessor

class TextProcessor(FileProcessor):
    def process(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()

        # Return the content as it is, without any preprocessing
        return content

