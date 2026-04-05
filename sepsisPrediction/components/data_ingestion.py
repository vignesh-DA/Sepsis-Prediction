"""
Data Ingestion Component
"""
import os
import pandas as pd
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    raw_data_path: str = os.path.join('Sepsis_Data', 'raw')
    processed_data_path: str = os.path.join('Sepsis_Data', 'processed')

class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        """
        Initiate data ingestion process
        """
        pass
