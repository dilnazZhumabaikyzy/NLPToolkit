from preprocess_builder import PreprocessBuilder

class TopicModelingBuilder(PreprocessBuilder):
    def __init__(self, nlp):
        super().__init__(nlp)
        self.steps = ['lowercase', 'remove_numbers', 'remove_symbols', 'tokenizer', 'remove_stopwords', 'lemmatize','trim_whitespace']

    def build(self):
        return self.process
