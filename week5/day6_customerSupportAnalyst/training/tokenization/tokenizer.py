import torch
from torch.utils.data import Dataset
from transformers import DistilBertTokenizerFast
from training.configs.training_config import TrainingConfig

class SupportDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        # Use 'labels' key so DistilBertForSequenceClassification computes loss natively
        item['labels'] = torch.tensor(self.labels[idx], dtype=torch.long)
        return item

    def __len__(self):
        return len(self.labels)

def tokenize_and_create_datasets(train_data, val_data):
    X_train, y_train_i = train_data
    X_val, y_val_i = val_data
    
    tokenizer = DistilBertTokenizerFast.from_pretrained(TrainingConfig.MODEL_NAME)
    
    train_encodings = tokenizer(X_train, truncation=True, padding=True, max_length=TrainingConfig.MAX_LENGTH)
    val_encodings = tokenizer(X_val, truncation=True, padding=True, max_length=TrainingConfig.MAX_LENGTH)
    
    train_dataset = SupportDataset(train_encodings, y_train_i)
    val_dataset = SupportDataset(val_encodings, y_val_i)
    
    return train_dataset, val_dataset, tokenizer
