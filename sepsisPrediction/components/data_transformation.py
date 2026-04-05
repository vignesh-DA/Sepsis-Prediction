"""
Data Transformation Component
"""
from sklearn.preprocessing import StandardScaler
from dataclasses import dataclass
import os

@dataclass
class DataTransformationConfig:
    preprocessor_path: str = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()
    
    def initiate_data_transformation(self, train_path, test_path):
        """
        Initiate data transformation process
        """
        pass
