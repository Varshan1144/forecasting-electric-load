import pandas as pd

def load_series(path_csv: str, ts_col: str = "timestamp", y_col: str = "load") -> pd.DataFrame:
    """
    Load a time series from CSV.
    
    Parameters:
    ----------
    path_csv : str
        Path to the CSV file
    ts_col : str
        Name of the timestamp column
    y_col : str
        Name of the target column (e.g., load, demand)

    Returns:
    -------
    pd.DataFrame
        DataFrame indexed by timestamp with a single column 'y'
    """
    df = pd.read_csv(path_csv, parse_dates=[ts_col])
    df = df.rename(columns={ts_col: "ds", y_col: "y"}).set_index("ds").sort_index()
    return df
