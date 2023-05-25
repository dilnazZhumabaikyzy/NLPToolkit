import pandas as pd
from ..tfidf_processor import TFIDFProcessor

# Decorator class to add additional functionality
class AdditionalFunctionalityDecorator(TFIDFProcessor):
    def __init__(self, tfidf_processor):
        self.tfidf_processor = tfidf_processor

    def calculate_tfidf(self, text_column):
        # Perform additional functionality
        additional_functionality_data = self.perform_additional_functionality(text_column)

        # Call the calculate_tfidf method of the decorated object
        tfidf_result = self.tfidf_processor.calculate_tfidf(text_column)

        # Perform additional operations on tfidf_result based on additional_functionality_data
        tfidf_result['additional_feature'] = additional_functionality_data

        return tfidf_result

    def perform_additional_functionality(self, text_column):
        # Perform additional functionality
        additional_functionality_data = self.tfidf_processor.df[text_column].apply(lambda x: len(x.split()))

        return additional_functionality_data
