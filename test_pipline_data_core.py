import pytest
import numpy as np
from numpy import nan
import pandas as pd

df = pd.read_excel(r'.\Product.xlsx')


# check if column exist
def test_col_exist():
    name = "ProductKey"
    assert name in df.columns
