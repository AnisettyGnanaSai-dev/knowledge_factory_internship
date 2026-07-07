import torch
from torch.utils.data import DataLoader
from sklearn.metrics import classification_report, accuracy_score, precision_recall_fscore_support, confusion_matrix
import numpy as np
import os
import joblib
from transformers import DistilBertForSequenceClassification

from training.configs.training_config import TrainingConfig

def evaluate_model(val_dataset, encoders):
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    print(f"Using device: {device} for evaluation.")
    
    val_loader = DataLoader(val_dataset, batch_size=TrainingConfig.BATCH_SIZE)
    
    model_path = TrainingConfig.OUTPUT_DIR
    if not os.path.exists(model_path):
        print("Model not found! Ensure training completed.")
        return
        
    print("Loading exported model for evaluation...")
    model = DistilBertForSequenceClassification.from_pretrained(
        model_path, 
        num_labels=len(encoders['intent'].classes_)
    )
    model.to(device)
    model.eval()
    
    all_intent_preds, all_intent_labels = [], []
    
    print("Evaluating...")
    with torch.no_grad():
        for batch in val_loader:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels']
            
            outputs = model(input_ids=input_ids, attention_mask=attention_mask)
            
            intent_preds = torch.argmax(outputs.logits, dim=1).cpu().numpy()
            
            all_intent_preds.extend(intent_preds)
            all_intent_labels.extend(labels.numpy())
            
    # Calculate detailed metrics
    acc = accuracy_score(all_intent_labels, all_intent_preds)
    precision, recall, f1, _ = precision_recall_fscore_support(all_intent_labels, all_intent_preds, average='weighted', zero_division=0)
    cm = confusion_matrix(all_intent_labels, all_intent_preds)
    
    print("\n" + "="*50)
    print("INTENT CLASSIFICATION METRICS")
    print("="*50)
    print(f"Accuracy:  {acc:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")
    
    print("\n" + "="*50)
    print("CONFUSION MATRIX")
    print("="*50)
    print(cm)
    
    print("\n" + "="*50)
    print("DETAILED CLASSIFICATION REPORT")
    print("="*50)
    print(classification_report(all_intent_labels, all_intent_preds, target_names=encoders['intent'].classes_, zero_division=0))
