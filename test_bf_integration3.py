import pandas as pd
from pandas_datareader import wb

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data = wb.download(indicator='FP.CPI.TOTL.ZG', country='all', start=2018, end=2020).reset_index()

data = data[147:]

data.head()

inflation = data.pivot_table(index='country', columns='year', values='FP.CPI.TOTL.ZG').reset_index()
inflation.head()


inflation['Evol_Inflation'] = round(((inflation['2020']-inflation['2018'])/inflation['2018'])*100, 2)
inflation['test_rows_averaging_last_years'] = round(inflation['2019']-inflation['2018'])

#print(inflation.head(300))

#print(inflation['Evol_Inflation'])

val_is_null = pd.isnull(inflation['Evol_Inflation'])

good_values = inflation['Evol_Inflation'][val_is_null == False]



#print(good_values)

average_inflation = sum(good_values) / len(good_values)

#print(average_inflation)


val_is_null = pd.isnull(inflation['Evol_Inflation'])

good_values = inflation['Evol_Inflation'][val_is_null == False]
NaN_values = inflation['Evol_Inflation'][val_is_null == True]

print(inflation['Evol_Inflation'][val_is_null == True])

#print(good_values)

average_inflation = sum(good_values) / len(good_values)

#print(average_inflation)

