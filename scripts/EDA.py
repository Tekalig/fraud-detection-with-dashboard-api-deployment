from src.data_processing import load_data, check_missing_values, handle_missing_data

def run_handle_missing_data(file_path):
    # load data
    df = load_data(file_path)

    # Display the first few rows of the DataFrame
    print(df.head())

    # Display the info of the DataFrame
    print(df.info())

    # Check for missing values
    print(check_missing_values(df))

    # handle missing data
    df = handle_missing_data(df)


# file path for Fraud data
file_path1 = '../data/Fraud_Data.csv'
file_path2 = '../data/creditcard.csv'

if __name__ == '__main__':
    run_handle_missing_data(file_path1)
    run_handle_missing_data(file_path2)

