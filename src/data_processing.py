import pandas as pd
from sklearn.impute import SimpleImputer

def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded DataFrame.
    """
    return pd.read_csv(file_path)

def check_missing_values(df):
    """
    Check for missing values in the DataFrame.

    Parameters:
    - df (pd.DataFrame): DataFrame to check for missing values.

    Returns:
    - bool: True if missing values are found, False otherwise.
    """
    return df.isnull().sum()

def handle_missing_data(df, strategy_num='mean', strategy_cat='most_frequent'):
    """
    Handle missing data in the DataFrame using sklearn SimpleImputer.

    Parameters:
    - df (pd.DataFrame): DataFrame with missing data.
    - strategy_num (str, optional): Strategy for imputing numerical data. Default is 'mean'.
    - strategy_cat (str, optional): Strategy for imputing categorical data. Default is 'most_frequent'.

    Returns:
    - pd.DataFrame: DataFrame with missing data handled.
    """
    # Separate numerical and categorical columns
    num_cols = df.select_dtypes(include=['number']).columns
    cat_cols = df.select_dtypes(include=['object', 'category']).columns

    # Impute numerical columns
    if not num_cols.empty:
        imputer_num = SimpleImputer(strategy=strategy_num)
        df[num_cols] = imputer_num.fit_transform(df[num_cols])

    # Impute categorical columns
    if not cat_cols.empty:
        imputer_cat = SimpleImputer(strategy=strategy_cat)
        df[cat_cols] = imputer_cat.fit_transform(df[cat_cols])

    return df