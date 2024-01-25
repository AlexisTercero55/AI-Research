# mymodule.py

import pandas as pd

def csv2DataFrame(file_path):
    """

    Read data from a CSV file into a Pandas DataFrame securely.


    Parameters:

    - file_path (str): The path to the CSV file.


    Returns:

    - pd.DataFrame: The DataFrame containing the CSV data.
    """

    try:

        # Use 'pd.read_csv' to read the CSV file into a DataFrame

        df = pd.read_csv(file_path)


        # You can perform additional security checks here if needed


        # Returning the DataFrame
        return df


    except Exception as e:

        # Handle exceptions, log errors, or take appropriate actions

        print(f"Error reading CSV file: {e}")

        return None


# Example usage:

if __name__ == "__main__":

    file_path = '.\Research\Regressions\Linear regression\Restaurant_revenue.csv'

    data_frame = csv2DataFrame(file_path)

    if data_frame is not None:
        print("Data loaded successfully.")
        # Do further processing with the DataFrame if needed

        print(data_frame.head())
    else:

        print("Failed to load data. Check the error message for details.")

