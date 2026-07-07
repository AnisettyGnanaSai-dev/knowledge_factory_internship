from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def clean_and_encode(df):
    """Encodes labels and splits the dataset."""
    le_intent = LabelEncoder()
    df['intent_encoded'] = le_intent.fit_transform(df['intent'])
    
    # Split
    X_train, X_val, y_train_i, y_val_i = train_test_split(
        df['text'].tolist(),
        df['intent_encoded'].tolist(),
        test_size=0.2, # 20% validation
        random_state=42
    )
    
    encoders = {
        'intent': le_intent
    }
    
    train_data = (X_train, y_train_i)
    val_data = (X_val, y_val_i)
    
    num_labels = {
        'intent': len(le_intent.classes_)
    }
    
    return train_data, val_data, encoders, num_labels
