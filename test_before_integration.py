import pandas as pd
import re

pd.set_option('display.max_rows', None)

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

#print(gdp['Zone'])

#gdp['Zone'].str.replace(" \[\d{1,3}\]","")

#print(gdp['Zone'].str.replace(" \[\d{1,3}\]","", regex=True))

#gdp['Zone'] = gdp['Zone'].str.replace(" \[\d{1,3}\]","", regex=True)

#print(clean_text([' \[\d{1,3}\]'], str(gdp['Zone'])))
#replaced = re.sub(' \[\d{1,3}\]', '', str(gdp['Zone']))
#print(replaced)

#print(gdp)

#print(gdp.sort_values('Evol_gdp', ascending=False))



import pycountry
import gettext
import copy
eng_to_french = gettext.translation('iso3166', pycountry.LOCALES_DIR,languages=['fr'])
eng_to_french.install()
french_to_eng = copy.copy(eng_to_french) #Make a copy
french_to_eng._catalog = {} #Remove the catalog

for key in eng_to_french._catalog.keys():
    french_to_eng._catalog[eng_to_french._catalog[key]] = key #replace the key with the entry and vice versa

#Verify
_ = french_to_eng.gettext
#translated_string = _("Iles Salomon")
#print(translated_string) #This should print "Germany"




#######################################


import pandas as pd
from pandas_datareader import wb

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 10000)
pd.set_option('display.expand_frame_repr', False)


aliment_17 = pd.read_csv('DisponibiliteAlimentaire_2017.csv')
population = pd.read_csv('Population_2000_2018.csv')
gdp = pd.read_csv('gdp_2018_2020.csv')
inflation = wb.download(indicator='FP.CPI.TOTL.ZG',country='all',start=2018,end=2022).reset_index()

#print(aliment_17.head(3))

aliment_pivot = aliment_17.pivot(index=['Zone', 'Produit', 'Année'], columns='Élément', values='Valeur').reset_index()

#print(aliment_pivot.head(3))

liste_viande = ['Viande de Volailles']

aliment_viande = aliment_pivot[aliment_pivot['Produit'].isin(liste_viande)].reset_index()
#print(aliment_viande.head())

inflation = inflation[196:]
#inflation = inflation[196:]
print(inflation)

inflation = inflation.pivot_table(index="country",columns="year", values="FP.CPI.TOTL.ZG")

year_2018 = inflation['year'] == "2018"
year_2019 = inflation['year'] == "2019"
year_2020 = inflation['year'] == "2020"
year_2021 = inflation['year'] == "2021"




#print(inflation.head())


inflation.loc[inflation['2018'].isnull(),'2018'] = inflation['2020']

inflation.loc[inflation['2019'].isnull(),'2019'] = inflation['2018']
inflation.loc[inflation['2020'].isnull(),'2020'] = inflation['2019']
inflation.loc[inflation['2021'].isnull(),'2021'] = inflation['2020']

print(inflation[inflation.isna().any(axis=1)])

