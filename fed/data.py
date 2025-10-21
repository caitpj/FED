import pandas as pd

my_data_path = 'fed/raw_data/GDP_data_in_current_USD.csv'

def convert_csv_to_dataframe(file_path):
    return pd.read_csv(file_path)

# Display the first 5 rows of the DataFrame
df = convert_csv_to_dataframe(my_data_path)
print(df.head())