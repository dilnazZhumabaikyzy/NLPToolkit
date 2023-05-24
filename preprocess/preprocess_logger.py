import logging
from preprocess_observer import Observer
class PreprocessingLogger(Observer):
    def update(self, event):
        step = event['step']
        logging.info(f"Preprocessing step applied: {step}")
