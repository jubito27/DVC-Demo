import pandas as pd
import numpy as np
import os


def load_data(data_path: str) -> pd.DataFrame:
    df = pd.read_csv(data_path , index_col=0)
    df=df.iloc[: , 3:]
    df =  df[df['Length of Membership'] >3]
    return df

def save_data(df : pd.DataFrame) -> None:
    df.to_csv(os.path.join('/mnt/WindowsD/Artificial Intelligence/MLOPS/DVC/dvc_demo/data' , 'customer.csv'))

def main(data_path : str) -> None:
    df = load_data(data_path=data_path)
    save_data(df=df)


data_path = '/mnt/WindowsD/Artificial Intelligence/Datasets/ecommerce_customers.csv'
main(data_path=data_path)
