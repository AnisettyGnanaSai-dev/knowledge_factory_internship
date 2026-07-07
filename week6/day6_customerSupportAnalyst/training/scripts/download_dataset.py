import os
import pandas as pd
from datasets import load_dataset

def download_and_validate_dataset():
    dataset_id = "bitext/Bitext-customer-support-llm-chatbot-training-dataset"
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw"))
    output_path = os.path.join(output_dir, "bitext.csv")
    
    print(f"Downloading dataset: {dataset_id}")
    dataset = load_dataset(dataset_id, split="train")
    df = dataset.to_pandas()
    
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dataset downloaded and saved to: {output_path}")
    
    print("\n" + "="*50)
    print("DATASET VALIDATION REPORT")
    print("="*50)
    
    # 1. Total Rows & Columns
    print(f"Total Rows: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    
    # 2. Missing Values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # 3. Duplicates
    # The bitext dataset has instruction, intent, category, response, utterance.
    # Utterance is the input text.
    duplicates = df.duplicated(subset=['instruction', 'intent']).sum()
    print(f"\nExact Duplicate Rows (by instruction & intent): {duplicates}")
    
    # 4. Class Distribution
    print("\nIntent Class Distribution (Top 15):")
    if 'intent' in df.columns:
        print(df['intent'].value_counts().head(15))
    else:
        print("No 'intent' column found.")
        
    print("\nValidation complete. READY FOR PREPROCESSING.")

if __name__ == "__main__":
    download_and_validate_dataset()
