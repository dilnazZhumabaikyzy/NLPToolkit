from .file_processor import FileProcessor
import xml.etree.ElementTree as ET

class XMLProcessor(FileProcessor):
    def process(self, file_path):
        # print(f"Processing XML file: {file_path}")

        # Parse the XML file
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Extract the text content from desired tags
        content = ' '.join(tag.text.strip() for tag in root.iter('text'))

        return content