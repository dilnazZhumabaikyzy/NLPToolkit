from ..preprocess_builder import PreprocessBuilder
import spacy
class SentimentAnalysisBuilder(PreprocessBuilder):
    def __init__(self):
        self.steps = ['lowercase', 'remove_numbers','trim_whitespace', 'tokenizer']
        super().__init__(self.steps, spacy.load("en_core_web_sm"))

    def remove_symbols(self, text):
        symbols = ['@', '#']  # Define the symbols to remove
        text = ''.join([c for c in text if c not in symbols])
        return text

    def build(self):
        return self
