"""
Analysis functions for solar data
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_solar_trends(df):
    """
    Perform basic analysis on solar data
    
    Parameters:
    df (pandas.DataFrame): Solar data
    
    Returns:
    dict: Analysis results
    """
    results = {}
    
    if df is None:
        return results
    
    # Basic statistics
    results['basic_stats'] = df.describe()
    
    # Correlation analysis
    numeric_df = df.select_dtypes(include=[np.number])
    if not numeric_df.empty:
        results['correlation_matrix'] = numeric_df.corr()
    
    return results

def plot_solar_trends(df, save_path=None):
    """
    Create visualization plots for solar data
    
    Parameters:
    df (pandas.DataFrame): Solar data
    save_path (str): Path to save the plot
    """
    if df is None:
        return
    
    numeric_df = df.select_dtypes(include=[np.number])
    
    if len(numeric_df.columns) >= 2:
        plt.figure(figsize=(12, 8))
        
        # Create subplots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # Plot 1: Distribution of first numeric column
        if len(numeric_df.columns) > 0:
            axes[0, 0].hist(numeric_df.iloc[:, 0], bins=20, alpha=0.7)
            axes[0, 0].set_title(f'Distribution of {numeric_df.columns[0]}')
            axes[0, 0].set_xlabel(numeric_df.columns[0])
            axes[0, 0].set_ylabel('Frequency')
        
        # Plot 2: Correlation heatmap
        if len(numeric_df.columns) > 1:
            correlation_matrix = numeric_df.corr()
            sns.heatmap(correlation_matrix, annot=True, ax=axes[0, 1])
            axes[0, 1].set_title('Correlation Matrix')
        
        # Plot 3: Time series if datetime exists
        datetime_columns = df.select_dtypes(include=['datetime64']).columns
        if len(datetime_columns) > 0 and len(numeric_df.columns) > 0:
            for i, col in enumerate(datetime_columns[:1]):  # Take first datetime column
                axes[1, 0].plot(df[col], numeric_df.iloc[:, 0])
                axes[1, 0].set_title(f'{numeric_df.columns[0]} over Time')
                axes[1, 0].set_xlabel(col)
                axes[1, 0].set_ylabel(numeric_df.columns[0])
                axes[1, 0].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        
        plt.show()