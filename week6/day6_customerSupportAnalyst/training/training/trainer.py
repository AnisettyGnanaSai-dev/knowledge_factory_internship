import torch
from torch.utils.data import DataLoader
from transformers import DistilBertForSequenceClassification, AdamW, get_linear_schedule_with_warmup
from tqdm import tqdm
from training.configs.training_config import TrainingConfig
from training.export.model_exporter import export_model_artifacts

def train_and_evaluate(train_dataset, val_dataset, num_labels, tokenizer, encoders):
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    print(f"Using device: {device}")
    
    train_loader = DataLoader(train_dataset, batch_size=TrainingConfig.BATCH_SIZE, shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=TrainingConfig.BATCH_SIZE)
    
    print("Initializing Single-Label DistilBERT Model...")
    model = DistilBertForSequenceClassification.from_pretrained(
        TrainingConfig.MODEL_NAME,
        num_labels=num_labels['intent']
    )
    model.to(device)
    
    optimizer = AdamW(model.parameters(), lr=TrainingConfig.LEARNING_RATE)
    total_steps = len(train_loader) * TrainingConfig.EPOCHS
    scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=0, num_training_steps=total_steps)
    
    best_val_loss = float('inf')
    
    print(f"Starting training for {TrainingConfig.EPOCHS} epochs...")
    for epoch in range(TrainingConfig.EPOCHS):
        model.train()
        total_train_loss = 0
        
        loop = tqdm(train_loader, desc=f'Epoch {epoch + 1}/{TrainingConfig.EPOCHS}', leave=True)
        for batch in loop:
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].to(device)
            
            optimizer.zero_grad()
            outputs = model(
                input_ids=input_ids, attention_mask=attention_mask, labels=labels
            )
            loss = outputs.loss
            total_train_loss += loss.item()
            
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()
            loop.set_postfix(loss=loss.item())
            
        avg_train_loss = total_train_loss / len(train_loader)
        
        # Validation Loop
        model.eval()
        total_val_loss = 0
        with torch.no_grad():
            for batch in val_loader:
                input_ids = batch['input_ids'].to(device)
                attention_mask = batch['attention_mask'].to(device)
                labels = batch['labels'].to(device)
                
                outputs = model(
                    input_ids=input_ids, attention_mask=attention_mask, labels=labels
                )
                total_val_loss += outputs.loss.item()
                
        avg_val_loss = total_val_loss / len(val_loader)
        print(f"\nEpoch {epoch + 1} completed. Average Train Loss: {avg_train_loss:.4f} | Average Val Loss: {avg_val_loss:.4f}")
        
        # Save best model
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            print("Validation loss improved. Exporting model artifacts...")
            export_model_artifacts(model, tokenizer, encoders)
            
    return model
