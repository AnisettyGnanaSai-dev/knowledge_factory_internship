# Training Configuration
import os

class TrainingConfig:
    # Hyperparameters
    EPOCHS = 3
    BATCH_SIZE = 16
    LEARNING_RATE = 5e-5
    MAX_LENGTH = 128
    
    # Reproducibility
    RANDOM_SEED = 42
    
    # Model & Data Paths
    MODEL_NAME = "distilbert-base-uncased"
    DATA_PATH = "data/dataset.csv"
    OUTPUT_DIR = "models/saved_model"
    
    # Metadata
    MODEL_VERSION = "v1.1"
    DATASET_VERSION = "v1.0"
    
    @classmethod
    def ensure_output_dir(cls):
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)
