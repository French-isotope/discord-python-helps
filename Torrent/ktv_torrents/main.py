import os
import json
import torrentool as to
from pathlib import Path
import functools

with open("rights_files.json", "r") as f:
    rights_file = json.loads(f.read())

#print(rights_file)

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
            if any(f'.{extension}' in dir for extension in extensions):
                parent[dir]['accessible'] = False
        parent = parent[dir]


#print(json.dumps(d, indent=4))

# with open("rights_files.json", "w") as f:
#    f.write(json.dumps(d, indent=4))

print('\n')

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


def nested_get(dic, keys):
    for key in keys:
        dic = dic[key]
    return dic


def compare_nested_get(dic_file, dic_recreate, keys, extensions):
    dic_to_return = dict()
    for key in keys:
        if key in dic_recreate and not key in dic_file and any(f'.{extension}' in key for extension in extensions):
            dic_to_return[key] = {"accessible": False}

        if key in dic_file and not key in dic_recreate:
            dic_to_return[key] = {}

        if not key in dic_recreate and key in dic_file:
            print(f'removing : {dic_file[key]}')
            del dic_file[key]

    return dic_to_return


for resultat in result:
    print(resultat)
#    compare_nested_get(rights_file, d, resultat)

print("")

for resultat in result:
    print(nested_get(d, resultat))
    #    print(f'{path_to_files}/{"/".join(resultat)}')


print("")

for resultat in result:
    print(nested_get(rights_file, resultat))
    #    print(f'{path_to_files}/{"/".join(resultat)}')


def compare_keys_in_dict():
    dic_to_return = dict()
    pass

dict_to_test = dict()
print(f'1 {dict_to_test}')

dict_to_test['1988_-_shoju_sentai'] = {'saison_1': {}}
print(f'2 {dict_to_test}')

#dict_to_test = dict_to_test.__setitem__('saison_1', {})
#print(f'3 {dict_to_test}')

#{dict_to_test['1988_-_shoju_sentai'].__setitem__('saison_1', {})
#print(f'4 {dict_to_test}')

#dict_to_test2 = dict_to_test['saison_1']
#print(f'5 {dict_to_test2}')

dict_to_test = {'1988_-_shoju_sentai': {'saison_1': {'01.mp4': {}}}}

listitems = ['1988_-_shoju_sentai', 'saison_1', '01.mp4']


#dict_to_test = dict()
#print(f'1 {dict_to_test}')

dictb = {
            '01.mp4':
            {
                'accessible': False
            }
        }


def check_if_key_in_path_exist(key, listitems2, dict_to_test2):
    try:
        functools.reduce(lambda e, key: e[key], listitems2, dict_to_test2)
    except KeyError as e:
        print(f'KHEEEEEEEEEEEEY error : {e}')
        print(listitems2)
        return False
    else:
        #
        if key in functools.reduce(lambda e, key: e[key], listitems2, dict_to_test2):
            print('Ouiii khé')
            print(listitems2)
            return True
        else:
            print('ONO paké')
            print(listitems2)
            return False


new_list_for_test = list()
for item in listitems:
    print(f"key : {item}")
    new_list_for_test.append(item)
    check_if_key_in_path_exist(item, new_list_for_test[:-1], dict_to_test)



# reduce(lambda d,key: d[key],path,aDict).update(aSecondDict)
functools.reduce(lambda e, key: e[key], listitems, dict_to_test).update(dictb)
# reduce(dict.__getitem__,path,aDict).update(aSecondDict)

#functools.reduce(dict.__getitem__,path, dict_to_test).update(dictb)
print()
print(dict_to_test)

#print(rights_file)
#print(json.dumps(d, indent=4))

print("")


def compare_nested_keys(dic_json, dic_directory, paths, extensions, is_shared=False):
    dic_to_return = dict()
    for keys in paths:
        #        print(f'keys : {keys}')
        for key in keys:
            if key in dic_directory \
                    and any(extension in key for extension in extensions) \
                    and key in dic_json:
                print(f'la key {key}')
                dic_to_return = dic_json[key]
#                dic_json = dic_json[key]
#                dic_directory = dic_directory[key]

            if key in dic_directory \
                    and any(extension in dic_directory[key] for extension in extensions) \
                    and key not in dic_json:
                dic_to_return[key] = {'accessible': is_shared}

            if key in dic_directory \
                    and key in dic_json:
                print("key !:: " + key)
                dic_to_return[key] = {}
                dic_to_return = dic_to_return[key]
                dic_directory = dic_directory[key]
#                print("1" + dic_json)
#                dic_json = dic_json[key]
            if not key in dic_directory and key in dic_json:
                # 4/ key directory avec item en moins par rapport à key
                # 	--> supprimer item de la datastruct file = ne pas ajouter à la new datastruct
                pass

    print(dic_to_return)
#    print(extensions)


print("\n lolilol \n")


compare_nested_keys(rights_file, d, result, extensions)

