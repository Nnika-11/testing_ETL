import pytest
import numpy as np
from numpy import nan
import pandas as pd


@pytest.fixture()
def df():
    df = pd.read_excel(r'.\Product.xlsx')
    return df


# check if column exist
def test_col_exist(df):
    name = "ProductKey"
    assert name in df.columns
    name = "EnglishProductName"
    assert name in df.columns


# check for nulls
def test_null(df):
    assert np.where(df['ProductKey'].isnull())


# check values and unique
def test_unique_val(df):
    assert pd.Series(df['ProductKey']).is_unique


# check data type
def test_productkey_isint(df):
    assert (df['ProductKey'].dtype == int or df['ProductKey'].dtype == np.int64)


def test_productname_dtype_str(df):
    assert (df['EnglishProductName'].dtype == str or df['EnglishProductName'].dtype == 'O')
