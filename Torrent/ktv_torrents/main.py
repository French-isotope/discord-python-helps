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
                parent[dir]['torrent_file'] = ''
        parent = parent[dir]


result = []
path = []

from copy import copy

# à réétudier
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


def key_in_path(key, listitems2, dict_to_test2, debug=False):
    try:
        functools.reduce(lambda e, key: e[key], listitems2, dict_to_test2)
    except KeyError as e:
        if debug:
            print(f'KHEEEEEEEEEEEEY error : {e}')
        return False
    else:
        if key in functools.reduce(lambda e, key: e[key], listitems2, dict_to_test2):
            if debug:
                print('Ouiii khé')
            return True
        else:
            if debug:
                print('ONO paké')
            return False

print("")


def merging_dicts_without_removing(dict_dir, dict_json, extensions, debug=False):
    # copier le json du dict_dir 1 pour 1 puis checker dans le json pour chercher les valeurs
    dict_return = dict_dir.copy()
    print(f'\n\n\n {dict_json} \n\n\n')

    for path in result:
        # print(functools.reduce(lambda e, key: e[key], path, dict_dir))
        last_key = path[-1]

        try:
            functools.reduce(lambda e, key: e[key], path, dict_json)
        except KeyError as e:
            if debug:
                print(f'Key error : {e}')
            pass
        else:
            if last_key in functools.reduce(lambda e, key: e[key], path[:-1], dict_json):

                if functools.reduce(lambda e, key: e[key], path, dict_json)['accessible']:

                    print(f'1 : {functools.reduce(lambda e, key: e[key], path, dict_return)}')
                    #functools.reduce(lambda e, key: e[key], path, dict_return)['accessible'] = True
                    functools.reduce(lambda e, key: e[key], path, dict_return).update({'accessible': True})

                    print(f'2 : {functools.reduce(lambda e, key: e[key], path, dict_return)}')

                if not 'torrent_file' in functools.reduce(lambda e, key: e[key], path, dict_json):

                    print(f'yapa1 : {functools.reduce(lambda e, key: e[key], path, dict_return)}')
                    functools.reduce(lambda e, key: e[key], path, dict_return)['torrent_file'] = ''
                    print(f'yapa2 : {functools.reduce(lambda e, key: e[key], path, dict_return)}')

                elif 'torrent_file' in functools.reduce(lambda e, key: e[key], path, dict_json) \
                and not functools.reduce(lambda e, key: e[key], path, dict_json)['torrent_file'] == '':

                    print(f'ya1 : {functools.reduce(lambda e, key: e[key], path, dict_return)}')
                    functools.reduce(lambda e, key: e[key], path, dict_return)['torrent_file'] = functools.reduce(lambda e, key: e[key], path, dict_json)['torrent_file']
                    print(f'ya2 : {functools.reduce(lambda e, key: e[key], path, dict_return)}')

    return dict_return


print(result)

new_datastructure_rights = merging_dicts_without_removing(d, rights_file, extensions)

import random
import string

for path in result:
    if key_in_path("accessible", path, new_datastructure_rights, debug=False):
        if functools.reduce(lambda e, key: e[key], path, new_datastructure_rights)['accessible'] \
        and functools.reduce(lambda e, key: e[key], path, new_datastructure_rights)['torrent_file'] == '':
            print(f'Création du torrent pour {"_".join(path)}')
            source = string.ascii_letters + string.digits
            result_str = ''.join((random.choice(source) for i in range(32)))
            functools.reduce(lambda e, key: e[key], path, new_datastructure_rights)['torrent_file'] = f'{result_str.lower()}.torrent'

print(json.dumps(new_datastructure_rights, indent=4))


with open("rights_files.json", "w", encoding='utf-8') as f:
    json.dump(new_datastructure_rights, f, indent=4)
