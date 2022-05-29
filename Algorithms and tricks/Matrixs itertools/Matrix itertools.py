import itertools as it

# https://fr.wikipedia.org/wiki/Produit_cart%C3%A9sien
# https://docs.python.org/fr/3/library/itertools.html

str1 = ['000', '001']
str2 = ['002', '003']

prod = it.product(str1, str2)
prod_list = []

for i in prod:
    prod_list += [i]
    "or prod_list.append(i)"