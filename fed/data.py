import pandas as pd
from pathlib import Path


def convert_csv_to_dataframe(file_path: str) -> pd.DataFrame:
    '''
    This function reads in a CSV file and returns a pandas DataFrame.
    It only reads in rows from a selected

    Args:
    file_path: str
    '''
    path = Path(__file__).parent.parent/"fed"/"raw_data"/file_path
    return pd.read_csv(path)


# convert to tidy format
def wide_to_long(df: pd.DataFrame) -> pd.DataFrame:
    '''
    This functions uses pandas melt
    to convert the dataframe from wide to long format.
    It also prints a message if there are any null values in the dataframe.

     Args:
     df: pd.Dataframe #Assumes Country Name is in left hand column

     Returns
     df_long: pd.DataFrame
    '''

    df_long = pd.melt(
        df, id_vars=['Country Name'], var_name='year', value_name='gdp')

    # check for nulls
    if df_long.isnull().values.any() is True:
        print("There are nulls in the dataframe.")
    elif df_long.isnull().values.any() is False:
        print("There are no nulls in the dataframe.")
    else:
        print("The function could not check for nulls.")

    return df_long.sort_values(['Country Name', 'year'])
