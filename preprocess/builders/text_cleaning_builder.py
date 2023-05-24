from ..preprocess_builder import PreprocessBuilder
import spacy
class TextCleaningBuilder(PreprocessBuilder):
    def __init__(self):
        self.steps = ['lowercase', 'remove_numbers', 'remove_symbols','trim_whitespace']
        super().__init__(self.steps, spacy.load("en_core_web_sm"))

    def build(self):
        return self
