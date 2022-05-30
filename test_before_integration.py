import pandas as pd
import re

gdp = pd.read_csv('gdp_2018_2020.csv')

gdp = gdp[['Unnamed: 0','2018 [2018].1','2019 [2019].1','2020 [2020].1']]
gdp = gdp.rename(columns={'Unnamed: 0':'Zone','2018 [2018].1':2018,'2019 [2019].1':2019,'2020 [2020].1':2020})
gdp = gdp.iloc[1:,:]

gdp[2018] = gdp[2018].replace(",", "", regex=True)
gdp[2019] = gdp[2019].replace(",", "", regex=True)
gdp[2020] = gdp[2020].replace(",", "", regex=True)

gdp[2018] = gdp[2018].astype(float)
gdp[2019] = gdp[2019].astype(float)
gdp[2020] = gdp[2020].astype(float)

gdp['Evol_gdp']=round((gdp[2020]-gdp[2018])/gdp[2018]*100,2)

gdp.head(1)

#print(gdp['Zone'])

gdp['Zone'] = gdp['Zone'].replace("[", '@')

#for line in gdp['Zone']:
#    print(line.strip('[')[0])

#print(str(gdp['Zone']).strip("[")[0])


def clean_text(rgx_list, text):
    new_text = text
    for rgx_match in rgx_list:
        new_text = re.sub(rgx_match, '', new_text)
    return new_text

re.compile(f'([]+(\S*)({arg})+)').findall(gdp['Zone'])

