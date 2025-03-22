from ..models.analyse_data_models import AnalysisResults
from typing import cast

def analyze_data(df):
    """Run some basic analysis on the employee data"""
    # Quick check to make sure we have the required columns
    for col in ['Salary', 'Age', 'Office', 'Position']:
        if col not in df.columns:
            print(f"Warning: '{col}' column missing - analysis may be incomplete")
    
    # Build our analysis dict
    results = {
        'total_employees': len(df),
        'salary_stats': {
            'min': float(df['Salary'].min()),
            'max': float(df['Salary'].max()),
            'mean': float(df['Salary'].mean()),
            'median': float(df['Salary'].median())
        },
        'age_stats': {
            'min': int(df['Age'].min()),
            'max': int(df['Age'].max()),
            'mean': float(df['Age'].mean()),
            'median': float(df['Age'].median())
        },
        'employees_by_office': df['Office'].value_counts().to_dict(),
        'employees_by_position': df['Position'].value_counts().to_dict()
    }
    
    print("Analysis complete")
    return cast(AnalysisResults, results)