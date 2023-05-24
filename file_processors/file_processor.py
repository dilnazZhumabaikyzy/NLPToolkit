from abc import ABC, abstractmethod

class FileProcessor(ABC):
    @abstractmethod
    def process(self, file_path):
        pass
