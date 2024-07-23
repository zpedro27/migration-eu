import pandas as pd
import numpy as np

def preprocess_data(df: pd.DataFrame):
    df_cols = _split_first_col(df)
    df_num = _clean_numerical(df)
    return df_cols.join(df_num)

def _split_first_col(df: pd.DataFrame):
    col_to_split = df.columns[0]
    df_new_cols = df[col_to_split].str.split(",", expand=True)
    df_new_cols.columns = col_to_split.split(",")
    return df_new_cols

def _clean_numerical(df: pd.DataFrame):
    df_num = df[df.columns[1:]].replace(r"[a-zA-Z\s\:]", "", regex=True)   # remove all letters, spaces and :
    df_num = df_num.replace("", np.nan)
    df_num = df_num.astype(float)
    df_num.columns = [int(col.replace(" ", "")) for col in df_num.columns]  # remove space from column names
    return df_num