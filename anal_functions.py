import pandas as pd
import numpy as np
from datetime import datetime, date

def data_retreival(symbols_list):
    df_list= [pd.read_csv('data/' + symbol + '.csv') for symbol in symbols_list]
    df_sector_vwap = pd.DataFrame([df_list[i]['vwap'] for i in range(len(df_list))])
    df_sector_vwap = df_sector_vwap.T
    df_sector_vwap.columns = symbols_list

    df_sector_vwap.index = pd.to_datetime(df_list[0]['timestamp'], unit='ms')
    df_sector_vwap.index = pd.to_datetime(df_sector_vwap.index.date)

    return df_sector_vwap