import pandas as pd

from ..builders.text_cleaning_builder import TextCleaningBuilder


class PreprocessingAdapter:
    def __init__(self, data):
        self.data = data
        self.builder = TextCleaningBuilder()
        self.builder.build()

    def preprocess(self):
        preprocessed_data = {}

        for file_name, content in self.data.items():
            preprocessed_text = self.builder.process(content)
            preprocessed_data[file_name] = preprocessed_text

        df = pd.DataFrame(list(preprocessed_data.values()), columns=['text'], index=list(preprocessed_data.keys()))
        return df
