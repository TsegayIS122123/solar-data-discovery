"""
Data loading utilities for solar data analysis
"""

import pandas as pd
import numpy as np

def load_solar_data(file_path):
    """
    Load solar data from CSV file
    
    Parameters:
    file_path (str): Path to the data file
    
    Returns:
    pandas.DataFrame: Loaded solar data
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully loaded data with {len(data)} rows and {len(data.columns)} columns")
        return data
    except FileNotFoundError:
        print(f"File {file_path} not found. Please check the file path.")
        return None

def clean_solar_data(df):
    """
    Clean and preprocess solar data
    
    Parameters:
    df (pandas.DataFrame): Raw solar data
    
    Returns:
    pandas.DataFrame: Cleaned data
    """
    if df is None:
        return None
    
    # Remove duplicate rows
    df_clean = df.drop_duplicates()
    
    # Handle missing values
    numeric_columns = df_clean.select_dtypes(include=[np.number]).columns
    df_clean[numeric_columns] = df_clean[numeric_columns].fillna(df_clean[numeric_columns].mean())
    
    print(f"Data cleaning complete. Removed {len(df) - len(df_clean)} duplicates.")
    return df_clean