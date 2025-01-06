import pyodbc 
import pandas as pd
import pytest
from sqlalchemy import create_engine


#pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. 
#Other DBAPI2 objects are not tested. 
#Please consider using SQLAlchemy.

# def get_data_from_sql():
#     conn = pyodbc.connect(
#         Trusted_Connection = "Yes",
#         DRIVER='{ODBC Driver 17 for SQL Server}',
#         SERVER="DESKTOP-D9QH4PH",
#         DATABASE="HINDALCO"
#     )
#     cursor = conn.cursor()
#     query = "SELECT * FROM stock_data"
#     df = pd.read_sql(query,conn)
#     conn.close()
#     return df

def get_data_from_sql(): 
    engine = create_engine('mssql+pyodbc://DESKTOP-D9QH4PH/HINDALCO?driver=ODBC+Driver+17+for+SQL+Server', fast_executemany=True) 
    query = "SELECT * FROM stock_data" 
    df = pd.read_sql(query, engine) 
    return df

