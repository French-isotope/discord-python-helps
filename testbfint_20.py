import json

clusters = "clusters.csv"
countries_by_clusters = dict()

with open(clusters, 'r', encoding='utf-8') as f:
    k_pays = f
    for line in k_pays:
        num, k, country = line.replace('"', '').split(',', maxsplit=2)
        if not k in countries_by_clusters and not k.isalpha():
            countries_by_clusters[k] = [country.strip('\n')]
        elif k in countries_by_clusters and not k.isalpha():
            countries_by_clusters[k].append(country.strip('\n'))

print(json.dumps(countries_by_clusters, indent=4, sort_keys=True, ensure_ascii=False))

