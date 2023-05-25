import unittest
import pandas as pd


from feature_extraction.tfidf_processor import TFIDFProcessor
from feature_extraction.decorators.additional_functionality_decorator import AdditionalFunctionalityDecorator


class TFIDFProcessorTest(unittest.TestCase):
    def setUp(self):
        data = {
            'text': ['one two three four.',
                     'Five six seven.',
                     'eight nine ten  ten ten ten.'] 
        }
        self.df = pd.DataFrame(data)
        self.tfidf_processor = TFIDFProcessor(self.df)

    def test_calculate_tfidf(self):
        tfidf_result = self.tfidf_processor.calculate_tfidf('text')
        self.assertIsInstance(tfidf_result, pd.DataFrame)
        self.assertEqual(tfidf_result.shape, (3, 10))  # Assuming there are 13 unique words in the text

class AdditionalFunctionalityDecoratorTest(unittest.TestCase):
    def setUp(self):
        data = {
            'text':['one two three four.',
                     'Five six seven.',
                     'eight nine ten  ten ten ten.'] 
        }
        self.df = pd.DataFrame(data)
        base_tfidf_processor = TFIDFProcessor(self.df)
        self.decorated_tfidf_processor = AdditionalFunctionalityDecorator(base_tfidf_processor)

    def test_calculate_tfidf_with_additional_functionality(self):
        tfidf_result = self.decorated_tfidf_processor.calculate_tfidf('text')
        self.assertIsInstance(tfidf_result, pd.DataFrame)
        self.assertEqual(tfidf_result.shape, (3, 11))  # Assuming there are 10 unique words + 1 additional feature

if __name__ == '__main__':
    unittest.main()