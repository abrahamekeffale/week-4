import pandas as pd
import numpy as np
from scipy import stats

def handle_missing_data(df):
    # Convert columns to numeric, forcing errors to NaN
    df['numeric_column'] = pd.to_numeric(df['numeric_column'], errors='coerce')
    # Fill NaN values with the median
    df['numeric_column'].fillna(df['numeric_column'].median(), inplace=True)
    return df

def remove_outliers(df: pd.DataFrame, threshold: float = 3.0):
    """
    Removes outliers using z-score.
    :param df: DataFrame to clean
    :param threshold: z-score threshold for identifying outliers
    :return: DataFrame with outliers removed
    """
    z_scores = np.abs(stats.zscore(df.select_dtypes(include=np.number)))
    return df[(z_scores < threshold).all(axis=1)]
