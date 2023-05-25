import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Base TF-IDF class
class TFIDFProcessor:
    def __init__(self, df):
        self.df = df
        self.vectorizer = TfidfVectorizer()

    def calculate_tfidf(self, text_column):
        preprocessed_data = self.df[text_column]

        # Calculate TF-IDF
        tfidf_matrix = self.vectorizer.fit_transform(preprocessed_data)

        # Get feature names (words)
        feature_names = self.vectorizer.get_feature_names_out()

        # Create a DataFrame from the TF-IDF matrix
        tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

        return tfidf_df
