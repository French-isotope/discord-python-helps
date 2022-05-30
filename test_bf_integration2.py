import pandas as pd


aliment_17 = pd.read_csv('DisponibiliteAlimentaire_2017.csv')
population = pd.read_csv('Population_2000_2018.csv')
gdp  = pd.read_csv('gdp_2018_2020.csv')

aliment_pivot = aliment_17.pivot(index=['Zone','Produit','Année'],columns='Élément',values='Valeur').reset_index()
aliment_pivot.head(3)

# liste_viande = ['Viande de Volailles','Viande de Bovins',"Viande d'Ovins/Caprins",'Viande de Suides','Viande, Autre']
liste_viande = ['Viande de Volailles']

aliment_viande = aliment_pivot[aliment_pivot['Produit'].isin(liste_viande)].reset_index()
aliment_viande.head()

population.head(3)

population_pivot = pd.pivot_table(data=population,index='Zone',columns='Année',values='Valeur').reset_index()
population_pivot.head()

population_pivot['evolution5Y'] = (population_pivot[2018] - population_pivot[2013])/population_pivot[2013]

population_pivot.head()

len(population_pivot.Zone.unique())

df = pd.merge(aliment_viande,population_pivot[['Zone',2017,'evolution5Y']],on='Zone', how='left')
df.head(3)

df = df[['Zone',2017,'Année','evolution5Y','Disponibilité alimentaire (Kcal/personne/jour)','Disponibilité intérieure', 'Exportations - Quantité',
       'Importations - Quantité', 'Nourriture','Pertes', 'Production']]
df.head()


len(df.Zone.unique())

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

gdp['Evol_gdp']=round((gdp[2020]-gdp[2018])/gdp[2018]*100,2)

gdp

# suprimer [2xx] du colone Zone
gdp['Zone'] = gdp['Zone'].str.rsplit(" ",n=1,expand=True)[0]

# 2 mme methode
# gdp['Zone'] = gdp['Zone'].str.replace(" \[\d{1,3}\]","", regex=True)

gdp = gdp.dropna()

gdp.isnull().sum()

len(gdp['Zone'].unique())

gdp.sort_values('Evol_gdp',ascending=False)
