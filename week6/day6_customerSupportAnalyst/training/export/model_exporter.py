import os
import joblib
import json
from datetime import datetime
from training.configs.training_config import TrainingConfig

def export_model_artifacts(model, tokenizer, encoders):
    """Exports trained model, tokenizer, label encoders, and metadata."""
    TrainingConfig.ensure_output_dir()
    
    # Save encoders
    joblib.dump(encoders['intent'], os.path.join(TrainingConfig.OUTPUT_DIR, 'le_intent.joblib'))
    
    # Save Tokenizer
    tokenizer.save_pretrained(os.path.join(TrainingConfig.OUTPUT_DIR, 'tokenizer'))
    
    # Save Model
    model.save_pretrained(TrainingConfig.OUTPUT_DIR)
    
    # Save Metadata
    metadata = {
        "model_version": TrainingConfig.MODEL_VERSION,
        "dataset_version": TrainingConfig.DATASET_VERSION,
        "training_date": datetime.utcnow().isoformat(),
        "training_config": {
            "model_name": TrainingConfig.MODEL_NAME,
            "epochs": TrainingConfig.EPOCHS,
            "batch_size": TrainingConfig.BATCH_SIZE,
            "learning_rate": TrainingConfig.LEARNING_RATE,
            "max_length": TrainingConfig.MAX_LENGTH,
            "random_seed": TrainingConfig.RANDOM_SEED
        },
        "supported_intents": encoders['intent'].classes_.tolist()
    }
    
    with open(os.path.join(TrainingConfig.OUTPUT_DIR, 'metadata.json'), 'w') as f:
        json.dump(metadata, f, indent=4)
        
    print(f"Artifacts and metadata successfully exported to {TrainingConfig.OUTPUT_DIR}")
