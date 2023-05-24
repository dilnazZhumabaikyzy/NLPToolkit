from .file_processor import FileProcessor
from bs4 import BeautifulSoup

class HTMLProcessor(FileProcessor):
    def process(self, file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        # Perform additional processing steps specific to HTML files
        processed_content = self._extract_html_tags(content)
      

        # Return the processed content
        return processed_content

    def _extract_html_tags(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        tag_list = ['h1', 'h2', 'h3', 'p', 'span']
        extracted_content = []

        for tag in tag_list:
            elements = soup.find_all(tag)
            for element in elements:
                extracted_content.append(element.get_text())

        # Join the extracted content with a space separator
        processed_content = ' '.join(extracted_content)
        return processed_content
