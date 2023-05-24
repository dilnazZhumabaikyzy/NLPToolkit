import unittest
from preprocess.adapters.preprocessing_adapter import PreprocessingAdapter

class PreprocessingAdapterTest(unittest.TestCase):
    def test_preprocess(self):
        # Define sample data
        data = {
            'file1': 'This is some text 123',
            'file2': 'Another example text 456'
        }

        # Create an instance of PreprocessingAdapter
        adapter = PreprocessingAdapter(data)

        # Perform preprocessing
        df = adapter.preprocess()

        # Assert the expected dataframe structure
        expected_columns = ['text']
        expected_index = ['file1', 'file2']
        self.assertListEqual(list(df.columns), expected_columns)
        self.assertListEqual(list(df.index), expected_index)

        # Assert the expected preprocessed text
        expected_text = ['this is some text', 'another example text']
        self.assertListEqual(list(df['text']), expected_text)

if __name__ == '__main__':
    unittest.main()
