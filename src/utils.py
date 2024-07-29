import os
import pandas as pd

# Directory where the data files will be stored
current_dir = os.path.dirname(__file__)
data_dir = os.path.join(current_dir, '..', 'data')

# Ensure the 'data' directory exists
os.makedirs(data_dir, exist_ok=True)


############################################################################################
############################## Data Load Utils #########################################
############################################################################################

def load_excel_data(name):
    """
    Load data from an Excel file with a dynamic name.

    Args:
    name (str): The dynamic part of the Excel file name to load.

    Returns:
    pd.DataFrame: The loaded data.
    """
    filename = f'DS_Homework_-_{name}.xlsx'
    file_path = os.path.join(data_dir, filename)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist. Please make sure the file is in the 'data' directory.")
    
    data = pd.read_excel(file_path, header=1, index_col=0)
    return data

# Example usage
if __name__ == "__main__":
    name = 'Accounts_Data_Final'  # Example dynamic part of the filename
    data = load_excel_data(name)
    # print(data.head())
