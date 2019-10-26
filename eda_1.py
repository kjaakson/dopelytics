#import csv
from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import seaborn as sns
import time
import requests

def read_partial_file(filepath,year):
    spending_df = pd.read_csv(filepath)

def upload_DF_to_postgres(df_to_upload, table_name):
    db_name = input('Enter database name: ') #prompt user for existing db name
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost/'+db_name) #create connection to db
    start = time.time()
    df_to_upload.to_sql(table_name, engine, chunksize=50000, method="multi")
    end = time.time()
    print(end-start)
    return(end-start)

def filter_data(input_DF,states,dollar_range):
    filtered_DF1 = input_DF[input_DF.recipient_state_code.isin(states)]
    filtered_DF2 = filtered_DF1[(filtered_DF1.total_dollars_obligated>dollar_range[0])&(filtered_DF1.total_dollars_obligated<dollar_range[1])]
    return filtered_DF2
