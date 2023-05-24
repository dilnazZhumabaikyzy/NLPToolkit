class PreprocessBuilder:
    def __init__(self, steps, nlp):
        self.steps = steps
        self.nlp = nlp

    def process(self, text):
        for step in self.steps:
            if step == "lowercase":
                text = text.lower()
            elif step == "trim_whitespace":
                text = text.strip()
            elif step == "remove_numbers":
                text = ''.join([c for c in text if not c.isdigit()])
            elif step[0] == "remove_symbols":
                symbols = step[1]
                if symbols:
                    text = ''.join([c for c in text if c not in symbols])
                else:
                    text = ''.join([c for c in text if not c.isalnum()])
            elif step == "tokenizer":
                text = text.split()  # Basic tokenization using whitespace
            elif step == "remove_stopwords":
                text = [token for token in text if token.lower() not in self.nlp.Defaults.stop_words]
            elif step == "lemmatize":
                text = [token.lemma_ for token in self.nlp(text)]
        return text
 