import torch
from training.data.dataset_loader import load_and_split_data
from training.preprocessing.text_cleaner import clean_and_encode
from training.tokenization.tokenizer import tokenize_and_create_datasets
from training.training.trainer import train_and_evaluate
from training.evaluation.evaluator import evaluate_model
from training.configs.training_config import TrainingConfig
import sys
import os
import random
import numpy as np
import torch

# Add the project root to sys.path to allow absolute imports from app.*
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

def main():
    print(f"Setting random seed to {TrainingConfig.RANDOM_SEED}...")
    set_seed(TrainingConfig.RANDOM_SEED)
    
    print("=== PHASE 1 & 2: DATASET CREATION & VALIDATION ===")
    df = load_and_split_data()
    print(f"Loaded {len(df)} samples.")
    
    print("\n=== PHASE 3: PREPROCESSING ===")
    train_data, val_data, encoders, num_labels = clean_and_encode(df)
    print("Labels encoded and data split.")
    
    print("\n=== PHASE 4: TOKENIZATION ===")
    train_dataset, val_dataset, tokenizer = tokenize_and_create_datasets(train_data, val_data)
    print("Tokenization complete.")
    
    print("\n=== PHASE 5: FINE-TUNING & EXPORT ===")
    model = train_and_evaluate(train_dataset, val_dataset, num_labels, tokenizer, encoders)
    print("Training and Export complete.")
    
    print("\n=== PHASE 6: EVALUATION ===")
    evaluate_model(val_dataset, encoders)
    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
