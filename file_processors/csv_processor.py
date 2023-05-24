import csv
from .file_processor import FileProcessor

class CSVProcessor(FileProcessor):
    def process(self, file_path):
        # Logic to process CSV file
        # print(f"Processing CSV file: {file_path}")

        with open(file_path, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.reader(csvfile)
            # Remove empty fields and join non-empty fields with a space
            content = " ".join(" ".join(field.strip() for field in row if field.strip()) for row in reader).strip()
        return content

