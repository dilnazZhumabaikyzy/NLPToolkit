from preprocess_builder import PreprocessBuilder

class NERBuilder(PreprocessBuilder):
    def __init__(self, nlp):
        super().__init__(nlp)
        self.steps = ['lowercase', 'tokenizer', 'ner','trim_whitespace']

    def ner(self, tokens):
        doc = self.nlp(' '.join(tokens))
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def build(self):
        return self.process
