def save_to_csv(df, file_path):
    """Save DataFrame to CSV file"""
    print(f"Saving to: {file_path}")
    
    try:
        df.to_csv(file_path, index=False)
        print(f"✓ Saved {len(df)} rows to {file_path}")
    except Exception as e:
        print(f"Error writing CSV: {e}")
        raise