from preprocess_builder import PreprocessBuilder

class TextCleaningBuilder(PreprocessBuilder):
    def __init__(self, nlp):
        super().__init__(nlp)
        self.steps = ['lowercase', 'remove_numbers', 'remove_symbols','trim_whitespace']

    def remove_symbols(self, text):
        symbols = ['@', '#', '$', '%']  # Define the symbols to remove
        text = ''.join([c for c in text if c not in symbols])
        return text

    def build(self):
        return self.process
