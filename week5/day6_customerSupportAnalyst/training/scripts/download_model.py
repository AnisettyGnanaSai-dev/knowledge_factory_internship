import os
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

def download_base_model():
    model_name = "distilbert-base-uncased"
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "models", "base_distilbert"))
    
    print(f"Downloading {model_name} to {output_dir}...")
    os.makedirs(output_dir, exist_ok=True)
    
    print("Downloading tokenizer...")
    tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)
    tokenizer.save_pretrained(output_dir)
    
    print("Downloading model weights...")
    model = DistilBertForSequenceClassification.from_pretrained(model_name)
    model.save_pretrained(output_dir)
    
    print("Base model download complete!")

if __name__ == "__main__":
    download_base_model()
