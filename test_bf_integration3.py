import pandas as pd
from pandas_datareader import wb

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = wb.download(indicator='FP.CPI.TOTL.ZG',country='all',start=2016,end=2020).reset_index()

data = data[147:]

data.head()

inflation = data.pivot_table(index='country', columns='year', values ='FP.CPI.TOTL.ZG' ).reset_index()
inflation.head()

inflation['Evol_Inflation'] = round(((inflation['2020']-inflation['2018'])/inflation['2018'])*100,2)

print(inflation.head())