import pandas as pd
import os

def load_data(train_filename: str, test_filename: str):
    """
    Loads train and test datasets from csv files.
    :param train_filename: Filename of the train dataset (assumed to be in the same folder or relative path)
    :param test_filename: Filename of the test dataset (assumed to be in the same folder or relative path)
    :return: train_data, test_data
    """
    # Get the absolute path of the current directory (where the script is located)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create full paths for the train and test files
    train_path = os.path.join(current_dir, '..', 'Data', train_filename)
    test_path = os.path.join(current_dir, '..', 'Data', test_filename)
    
    # Load the CSV files into pandas DataFrames
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)
    
    return train_data, test_data

if __name__ == "__main__":
    # Load data using relative paths
    train_data, test_data = load_data('train.csv', 'test.csv')
    print("Train Data Sample:")
    print(train_data.head())
    print("\nTest Data Sample:")
    print(test_data.head())

