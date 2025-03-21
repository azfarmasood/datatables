import pandas as pd

def clean_data(df):
    """Cleans and transforms the data"""
    # Work on a copy
    df_clean = df.copy()
    
    # TODO: Add support for different date formats
    
    # Number conversions
    df_clean['Age'] = pd.to_numeric(df_clean['Age'])
    
    # Handle salary - This regex removes $ and commas
    if 'Salary' in df_clean.columns:
        df_clean['Salary'] = df_clean['Salary'].replace(r'[\$,]', '', regex=True).astype(float)
    
    # Convert dates
    if 'Start date' in df_clean.columns:
        df_clean['Start date'] = pd.to_datetime(df_clean['Start date'])
        
        # Calculate years employed
        today = pd.Timestamp.now()
        df_clean['Years Since Hiring'] = df_clean['Start date'].apply(lambda x: (today - x).days / 365.25).round(1)
    
    print("Data cleaned!")
    return df_clean
