"""
Model Training Component
"""
from dataclasses import dataclass
import os

@dataclass
class ModelTrainerConfig:
    model_path: str = os.path.join('models', 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()
    
    def initiate_model_training(self, train_arr, test_arr):
        """
        Initiate model training process
        """
        pass
