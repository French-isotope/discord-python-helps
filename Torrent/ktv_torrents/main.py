import os
import json
import torrentool as to
from pathlib import Path

with open("rights_files.json", "r") as f:
    rights_file = f.read().rstrip()

print(rights_file)

path_to_files = "C:/torrents_project"

arborescence = dict()

# create arborescence in datastructure
arr = []
for root, dirs, files in os.walk(path_to_files):
    for dir in dirs:
        if not dir in arborescence:
            arborescence[dir] = []

    for filename in files:
        sub_dir = root.split("/")[1:]
        arr.append(os.path.join(root, filename))


# correct paths
arr2 = []
for item in arr:
    if '/' in item:
        item = item.replace('/', '\\')
    arr2.append(item.replace('C:\\torrents_project\\', ''))


extensions = ['mp4', 'mkv', 'avi']

#
d = dict()
for path in arr2:
    parent = d
    for dir in path.split('\\'):
        if dir not in parent:
            parent[dir] = dict()
            if any(extension in dir for extension in extensions):
                parent[dir]['accessible'] = False
        parent = parent[dir]


print(json.dumps(d, indent=4))

#with open("rights_files.json", "w") as f:
#    f.write(json.dumps(d, indent=4))

print('\n\n\n')

result = []
path = []
from copy import copy


# i is the index of the list that dict_obj is part of
def find_path(dict_obj, i=None):
    for k, v in dict_obj.items():
        # add key to path
        path.append(k)
        if isinstance(v, dict):
            # continue searching
            find_path(v, i)
        if isinstance(v, list):
            # search through list of dictionaries
            for i, item in enumerate(v):
                # add the index of list that item dict is part of, to path
                path.append(i)
                if isinstance(item, dict):
                    # continue searching in item dict
                    find_path(item, i)
                # if reached here, the last added index was incorrect, so removed
                path.pop()
        if type(v) == dict:
            if 'accessible' in v.keys():
                # add path to our result
                result.append(copy(path))

        # remove the key added in the first line
        if path != []:
            path.pop()


# default starting index is set to None
find_path(d)

print("\n\n\n\n\n\n")
#print(d)
print("\n\n\n\n\n\n")


def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


for resultat in result:
#    print(resultat)
    print(f'{path_to_files}/{"/".join(resultat)}')
    print(nested_get(d, resultat))

