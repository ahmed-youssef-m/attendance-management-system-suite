import pandas as pd


def search_for_number_in_excel_column(file_path, search_value, column_index=0):
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Error: Excel file '{file_path}' not found.")
        return False

    return df.iloc[:, column_index].isin([search_value]).any()


# Example usage
# file_path = "existing_file.xlsx"
# search_value = 30
#
# number_exists = search_for_number_in_excel_column(file_path, search_value)

# if number_exists:
#     print(f"The number {search_value} exists in the first column of the Excel file.")
# else:
#     print(f"The number {search_value} does not exist in the first column of the Excel file.")
