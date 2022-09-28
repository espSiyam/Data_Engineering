import pandas as pd


def table(connection, table_name):
    sql = f'''select * from {table_name}'''
    df = pd.read_sql(sql,con=connection)
    return df