from abc import ABC, abstractmethod

# Abstract base class for handlers
class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass
    
    @abstractmethod
    def handle_request(self, request):
        pass