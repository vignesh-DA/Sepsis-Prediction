"""
Training Pipeline
"""
from sepsisPrediction.components.data_ingestion import DataIngestion
from sepsisPrediction.components.data_transformation import DataTransformation
from sepsisPrediction.components.model_trainer import ModelTrainer

class TrainingPipeline:
    def __init__(self):
        pass
    
    def run_pipeline(self):
        """
        Execute the complete training pipeline
        """
        # Data Ingestion
        data_ingestion = DataIngestion()
        
        # Data Transformation
        data_transformation = DataTransformation()
        
        # Model Training
        model_trainer = ModelTrainer()
        
        print("Training pipeline completed")

if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run_pipeline()
