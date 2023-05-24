from .preprocess_observer import Subject
from .preprocess_builder import PreprocessBuilder
import spacy

class Preprocess:
    def __init__(self):
            self.steps = []
            self.subject = Subject()
            self.nlp = spacy.load("en_core_web_sm")  # Load the spaCy English model

    def lowercase(self):
            self.steps.append("lowercase")
            self.subject.notify_observers('lowercase')
            return self
    
    def trim_whitespace(self):
        self.steps.append("trim_whitespace")
        self.subject.notify_observers('trim_whitespace')
        return self

    def remove_numbers(self):
            self.steps.append("remove_numbers")
            self.subject.notify_observers('remove_numbers')
            return self

    def remove_symbols(self, symbols=None):
            self.steps.append(("remove_symbols", symbols))
            self.subject.notify_observers('remove_symbols')
            return self

    def tokenizer(self):
            self.steps.append("tokenizer")
            self.subject.notify_observers('tokenizer')
            return self

    def remove_stopwords(self):
            self.steps.append("remove_stopwords")
            self.subject.notify_observers('remove_stopwords')
            return self

    def lemmatize(self):
            self.steps.append("lemmatize")
            self.subject.notify_observers('lemmatize')
            return self

    def build(self):
            return PreprocessBuilder(self.steps, self.nlp)
