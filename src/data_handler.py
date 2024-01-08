import pandas as pd


def save_data(data, source):
    """
    Saves the discount data to a file.
    """
    df = pd.DataFrame(data)
    df.to_csv(f'{source}_discounts.csv', index=False)


def load_data(source):
    """
    Loads the discount data from a file.
    """
    try:
        df = pd.read_csv(f'{source}_discounts.csv')
        return df
    except FileNotFoundError:
        print(f'No data file found for {source}.')
        return pd.DataFrame()
