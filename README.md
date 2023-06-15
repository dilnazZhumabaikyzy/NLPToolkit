# NLPToolkit: Data Processing Library

NLPToolkit is a Python library that provides various data processing functionalities, including file loading and text preprocessing. It employs several design patterns to achieve its functionality and provide a flexible and extensible architecture. . Here are the design patterns utilized in this project: 

## Builder Pattern: 
The Builder pattern is utilized in the TextCleaningBuilder class to construct a complex text cleaning process step by step. It provides a flexible and readable way to define the cleaning operations.

## Factory Method Pattern: 
The Factory Method pattern is used to handle different file types (.csv, .txt, .html, .json, .xml) in the DataProcessor class. It provides a way to create the appropriate file processor based on the file extension, allowing for extensibility and customization.

## Adapter Pattern: 
The Adapter pattern is employed in the PreprocessingAdapter class to adapt the preprocessing functionality to work with the existing TextCleaningBuilder. It facilitates the seamless integration of the preprocessing logic with the cleaning process.

## Decorator Pattern: 
The Decorator pattern is utilized in the AdditionalFunctionalityDecorator to extend the behavior of the TF-IDF processor by adding additional functionality, such as feature selection or dimensionality reduction.

## Observer Pattern: 
The Observer pattern is employed to implement a logging system for data preprocessing and monitoring. It allows observers to receive notifications and log relevant information during the preprocessing process.

## Chain of Responsibility Pattern: 
The Chain of Responsibility pattern is utilized in the FileLoadingHandler and PreprocessingHandler classes to create a chain of handlers. Each handler is responsible for processing a specific type of request. If a handler cannot process the request, it passes it to the next handler in the chain until the request is handled or an invalid request is encountered.

## Features

- File Loading: Load files from a specified directory, supporting different file types.
- Text Preprocessing: Preprocess text data using various cleaning and normalization techniques.
- Chain of Responsibility: Implement a chain of handlers to process requests sequentially.
- Adapter: Use adapters to adapt different preprocessing methods to a common interface.

## Directory Structure
The project follows a specific directory structure:

- `data_processing.py`: Contains the main data processing logic and entry point of the library.
- `feature_extraction.py`: Implements various feature extraction strategies, such as TF-IDF or Bag-of-Words.
- `handlers/`: Contains handler classes for file loading and preprocessing requests.
- `adapters/`: Contains adapter classes to adapt the preprocessing functionality.
- `builders/`: Includes builder classes for text cleaning process construction.
- `observers/`: Contains observer classes for logging and monitoring during preprocessing.
- `tests/`: Includes test files for unit testing different components of the library.

Feel free to explore the code and utilize the provided functionalities for your NLP tasks.

## Installation

To install DPProject, you can use pip:

```
pip install dpproject
```
## Usage
To use the library, follow these steps:

1. Import the necessary modules from the library.
2. Create instances of the appropriate classes based on your requirements.
3. Utilize the available methods and functions to process your text data, extract features, and perform other NLP tasks.
4. Handle the results as needed for your specific use case.

For detailed examples and usage instructions, refer to the documentation provided within each module or consult the example files in the `tests/` directory.

Please note that this library is still under development, and further enhancements and features will be added in future updates.

Contributions, bug reports, and feature requests are welcome. Feel free to open issues or submit pull requests on the GitHub repository.

Enjoy using the NLP library!

### File Loading

```python
from dpproject.handlers.file_loading_handler import FileLoadingHandler

# Create the handler
handler = FileLoadingHandler()

# Send file_loading request
handler.handle_request('file_loading')
```

### Text Preprocessing

```python
from dpproject.handlers.preprocessing_handler import PreprocessingHandler

# Create the handler
handler = PreprocessingHandler()

# Send preprocessing request
handler.handle_request('preprocessing')
```

For more examples and detailed usage instructions, please refer to the documentation.

## Contributing

Contributions to DPProject are welcome! If you find a bug, have suggestions for improvement, or want to add new features, please submit an issue or a pull request on the GitHub repository.


## Unit Tests

Unit tests have been implemented to ensure the correctness of the library's components. To run the unit tests, follow these steps:

1. Make sure you have all the necessary dependencies installed. You can check the `requirements.txt` file for the required packages and their versions.

2. Open a terminal or command prompt and navigate to the root directory of the project.

3. Run the following command to execute the unit tests:

   ```bash
   python -m unittest discover tests
   ```

   This command will automatically discover and run all the test files located in the `tests/` directory.

4. After running the tests, the test results will be displayed in the terminal, indicating which tests passed or failed.

It is recommended to run the unit tests regularly to ensure the stability and reliability of the library. If you encounter any issues or failures during the tests, please report them on the GitHub repository.

Feel free to extend the existing tests or add new tests to cover additional scenarios as needed.

## Test Data

The unit tests rely on test data located in the `tests/test_data/` directory. This data is used to simulate different input scenarios and verify the expected outputs. Ensure that the test data is properly set up and accessible before running the unit tests.

Please note that the unit tests are designed to validate the functionality of the library and may take some time to complete depending on the complexity of the tests and the amount of test data used.

Running the unit tests regularly will help maintain the quality and correctness of the library.
