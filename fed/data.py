import pandas as pd

my_data_path = 'fed/raw_data/GDP_data_in_current_USD.csv'

def convert_csv_to_dataframe(file_path):
    """Convert a CSV file to a pandas DataFrame."""
    return pd.read_csv(file_path)

df = convert_csv_to_dataframe(my_data_path)

# Display the first 5 rows of the DataFrame - can delete later, just used for testing
print(df.head())

# convert to tidy format
def wide_to_long(df):
    ''' 
    Use pandas melt to convert the dataframe from wide to long format
    Assumes the data has Country Name in the left hand column, and then columns for each year showing GDP
    '''
    df = pd.melt(df, id_vars=['Country Name'], var_name = 'year', value_name = 'gdp')
    return df

df_long = wide_to_long(df)

# Display the first 5 rows of the DataFrame - can delete later, just used for testing
print(df_long.head())

# handle nulls
# since there are none in this data, could delete
def isnull_any(df):
    '''returns if there are any null values in each column'''
    return df.isnull().any()
print(isnull_any(df_long))


