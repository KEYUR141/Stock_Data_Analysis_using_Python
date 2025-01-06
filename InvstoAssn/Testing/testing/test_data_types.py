import pytest
import pandas as pd
from sources.data_fetch import get_data_from_sql

@pytest.fixture
def sql_data():
    return get_data_from_sql()

def test_datetime(sql_data):
    df = sql_data
    assert pd.api.types.is_datetime64_any_dtype(df['datetime']), "datetime column is not of datetime type"

def test_decimal(sql_data):
    df = sql_data
    for col in ['open','high','low','close']:
        assert pd.api.types.is_float_dtype(df[col]), f"{col} column is not of decimal type"

def test_string(sql_data):
    df = sql_data
    assert pd.api.types.is_string_dtype(df['instrument']), "Instrument column is not of string type"

def test_int(sql_data):
    df = sql_data
    assert pd.api.types.is_integer_dtype(df['volume']), "Volume column is not of integer type"