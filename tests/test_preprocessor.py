import unittest
from preprocess.preprocess import Preprocess
from preprocess.builders.sentiment_analysis_builder import SentimentAnalysisBuilder
import logging
from io import StringIO

logging.basicConfig(level=logging.INFO)  # Configure logging level and format



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

        # # Capture logging messages
        # stream = StringIO()
        # handler = logging.StreamHandler(stream)
        # logging.getLogger().addHandler(handler)

        # # Your preprocessing code here...

        # # Remove the handler and get the captured logs
        # logging.getLogger().removeHandler(handler)
        # handler.close()
        # logs = stream.getvalue().strip()

        # # Display the captured logs
        # print(logs)

        self.assertEqual(processed_text, expected_text)

    def test_sentiment_analysis(self):
        # Create an instance of the SentimentAnalysisBuilder
        builder = SentimentAnalysisBuilder()

        # Build the sentiment analysis function
        sentiment_analyzer = builder.build()

        # Test the sentiment analysis
        text = "This is a great movie!"
        sentiment_scores = sentiment_analyzer.process(text)

        # Assert the expected sentiment scores
        expected_scores = ['this', 'is', 'a', 'great', 'movie!']
        self.assertEqual(sentiment_scores, expected_scores)

if __name__ == '__main__':
    unittest.main()
