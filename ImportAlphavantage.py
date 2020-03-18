#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas as pd

#ts = timeseries.TimeSeries(key='9ZKFFW6UKXX3Q2TZ', output_format='pandas')
#data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
symbol = ''+sys.argv[1]+''

class TechnicalIndicators:
    def __init__(self):
        self.api_key='9ZKFFW6UKXX3Q2TZ'
        self.symbol_name=self.symbol()
        self.macd_data=self.macd()
        self.rsi_data=self.rsi()
        self.bbands_data=self.bbands()
        self.close_data=self.close()
        self.sma_data=self.sma()
    def symbol(self):
        symbol_name=symbol
        return symbol_name
    def macd(self):
        a = TechIndicators(key=self.api_key, output_format='pandas')
        data, meta_data= a.get_macd(symbol=self.symbol_name,interval='daily')
        return data
    def bbands (self):
        c=TechIndicators(key=self.api_key,output_format='pandas')
        data,meta_data=c.get_bbands(symbol=self.symbol_name)
        return data
    def rsi(self):
        b=TechIndicators(key=self.api_key,output_format='pandas')
        data,meta_data = b.get_rsi(symbol=self.symbol_name,interval='daily',time_period=14)
        return data
    def sma(self):
        d= TechIndicators(key=self.api_key, output_format='pandas')
        data, meta_data = d.get_sma(symbol=self.symbol_name,time_period=30)
        return data
    
if __name__ == "__main__":
    TI=TechnicalIndicators()
    rsi_data = TI.rsi_data
    macd_data = TI.macd_data
    bbands_data = TI.bbands_data
    sma_data = TI.sma_data
    plt.plot(sma_data)
    plt.plot(bbands_data)
    plt.plot(macd_data)
    plt.plot(rsi_data)
    plt.show()

data=rsi_data.merge(sma_data,left_index=True,right_index=True)
data['Symbol']=symbol
data=data.merge(bbands_data,left_index=True,right_index=True)
data=data.merge(macd_data,left_index=True,right_index=True)
"""
user='python'
pwd='pythonpwd'
database='@localhost/bigquery'
psql_connect='postgresql://'+user+':'+pwd+database

engine = create_engine(psql_connect)
data.to_sql('testMSFT', engine, if_exists='append')

data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()



data=pd.read_csv("/home/thibaud/Documents/BigQuery/daily_adjusted_MSFT.csv")
from sqlalchemy import create_engine
engine = create_engine('postgresql://python:pythonpwd@localhost/bigquery')
data.to_sql('alphavantage', engine, if_exists='append')
"""