import unittest
from preprocess.preprocess import Preprocess
from preprocess.builders.sentiment_analysis_builder import SentimentAnalysisBuilder

class PreprocessTestCase(unittest.TestCase):
    def test_custom_preprocessing(self):
        # Create an instance of Preprocess
        preprocessor = Preprocess()

        # Customize the preprocessing steps
        preprocessor.lowercase()
        preprocessor.remove_numbers()
        preprocessor.trim_whitespace()

        # Build the final preprocessing function
        custom_preprocess = preprocessor.build()

        # Test the custom preprocessing
        text = "This is a Sample Text 123"
        processed_text = custom_preprocess.process(text)

        # Assert the expected processed text
        expected_text = "this is a sample text"
        self.assertEqual(processed_text, expected_text)

    def test_sentiment_analysis(self):
        # Create an instance of the SentimentAnalysisBuilder
        builder = SentimentAnalysisBuilder()

        # Customize the preprocessing steps
        builder.lowercase()
        builder.remove_numbers()

        # Build the sentiment analysis function
        sentiment_analyzer = builder.build()

        # Test the sentiment analysis
        text = "This is a great movie!"
        sentiment_scores = sentiment_analyzer.process(text)

        # Assert the expected sentiment scores
        expected_scores = {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.6249}
        self.assertEqual(sentiment_scores, expected_scores)

if __name__ == '__main__':
    unittest.main()
