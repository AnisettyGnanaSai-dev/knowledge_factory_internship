import os
import pandas as pd

def preprocess_bitext_dataset():
    # Paths
    raw_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "raw", "bitext.csv"))
    final_output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data", "dataset.csv"))
    
    print("=== SupportSense AI Preprocessing ===")
    
    # 1. Load Raw Data
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Raw dataset not found at {raw_path}")
    
    df = pd.read_csv(raw_path)
    print(f"Loaded raw dataset: {len(df)} rows")
    
    # 2. Clean Data (Drop missing and exact duplicates based on the text instruction)
    df = df.dropna(subset=['instruction', 'intent'])
    df = df.drop_duplicates(subset=['instruction', 'intent'])
    print(f"After dropping duplicates & nulls: {len(df)} rows")
    
    # 3. Intent Rollup Mapping
    # We map the 27 Bitext intents into our 3 core system intents: billing, technical, general
    intent_mapping = {
        # Billing
        'check_invoice': 'billing',
        'check_payment_methods': 'billing',
        'payment_issue': 'billing',
        'get_invoice': 'billing',
        'get_refund': 'billing',
        'track_refund': 'billing',
        
        # Technical
        'edit_account': 'technical',
        'switch_account': 'technical',
        'registration_problems': 'technical',
        'create_account': 'technical',
        'delete_account': 'technical',
        'recover_password': 'technical',
        'change_shipping_address': 'technical',
        'set_up_shipping_address': 'technical',
        
        # General / Order Management / Customer Service
        'complaint': 'general',
        'contact_customer_service': 'general',
        'contact_human_agent': 'general',
        'delivery_period': 'general',
        'newsletter_subscription': 'general',
        'place_order': 'general',
        'cancel_order': 'general',
        'track_order': 'general',
        'check_cancellation_fee': 'general',
        'check_refund_policy': 'general',
        'delivery_options': 'general',
        'review': 'general',
        'get_receipt': 'billing' # Mapped to billing
    }
    
    # Apply mapping, dropping any rows that couldn't be mapped just in case
    df['mapped_intent'] = df['intent'].map(intent_mapping)
    df = df.dropna(subset=['mapped_intent'])
    
    # 4. Format for our application (text, intent)
    final_df = pd.DataFrame({
        'text': df['instruction'].str.strip(),
        'intent': df['mapped_intent']
    })
    
    # Shuffle the dataset so batches have mixed intents
    final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    # 5. Save Final Dataset
    os.makedirs(os.path.dirname(final_output_path), exist_ok=True)
    final_df.to_csv(final_output_path, index=False)
    
    print("\n=== Preprocessing Complete ===")
    print(f"Final Dataset Size: {len(final_df)} rows")
    print("New Class Distribution:")
    print(final_df['intent'].value_counts())
    print(f"\nSaved production-ready dataset to: {final_output_path}")

if __name__ == "__main__":
    preprocess_bitext_dataset()
