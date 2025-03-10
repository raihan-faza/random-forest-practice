from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split


def load_dataset() -> pd.DataFrame:
    df = pd.read_csv("pcos_dataset.csv")
    return df


def split_dataset(df: pd.DataFrame, test_size: float, random_state: int) -> Tuple:
    xtrain, xtest, ytrain, ytest = train_test_split(
        df, test_size=test_size, random_state=random_state
    )
    return xtrain, xtest, ytrain, ytest


def encode_data():
    return


def explore_dataset(df: pd.DataFrame):
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())
    print(df.select_dtypes(include=["object"]).nunique())


explore_dataset(load_dataset())
