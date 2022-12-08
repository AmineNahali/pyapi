from sqlalchemy import create_engine
import pandas as pd
import json

# MSSQL settings :
_Driver="SQL Server Native Client 11.0"
_Server="DESKTOP-9VQBAIB"
_Database="db1"
_Database_Con = f"mssql://@{_Server}/{_Database}?driver={_Driver}"
engine=create_engine(_Database_Con)

def mssql_prepare():
    con = engine.connect()
    df=pd.read_sql_query("CREATE TABLE DataTest(data varchar(1024));",con)
    df

def mssql_save_data(x):
    con = engine.connect()
    df=pd.read_sql_query(f"INSERT INTO DataSet data VALUES (\"{x}\");",con)
    df

#TODO: remove this ?
def mssql_show_data():
    con = engine.connect()
    df=pd.read_sql_query(f"SELECT data from DataSet;",con)
    df

def mssql_drop_db():
    con = engine.connect()
    df=pd.read_sql_query(f"DROP TABLE DataSet;",con)
    df