import os
import json
from pathlib import Path



path_to_files = "C:/torrents_project"

rights_files = dict()

for dir in os.listdir(path_to_files):
    if os.path.isdir(os.path.join(path_to_files, dir)):
        pass
#        print(dir)
    for subdir in os.listdir(os.path.join(path_to_files, dir)):
        if os.path.isdir(os.path.join(path_to_files, dir, subdir)):
            pass
#            print(dir + ' ' + subdir)

for root, dirs, files in os.walk(path_to_files):
#    print(f'dirs : {dirs}')
    for dir in dirs:
        if not dir in rights_files:
            rights_files[dir] = []

    for filename in files:
        pass
#        print(f'root :{root}')
#        print(os.path.join(root, filename))

#print(rights_files)


test_dict = dict()



def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            test = it.path.split('\\')[1:]
            if not test[0] in test_dict:
                test_dict[test[0]] = []
#                print(f'test : {test}')
            listdirs(it)

listdirs(path_to_files)

#print(json.dumps(test_dict, indent=4))


"""
def listdirs(rootdir):
    for path in Path(rootdir).iterdir():
        if path.is_dir():
            print(path)
            listdirs(path)


listdirs(path_to_files)
"""

test_dict2 = dict()

def create_subdirs_in_dict(split_dir):
    for dir in split_dir:
        test_dict2


arr = []
for root, dirs, files in os.walk(path_to_files):
    for dir in dirs:
        if not dir in rights_files:
            rights_files[dir] = []

    for filename in files:
        sub_dir = root.split("/")[1:]
        arr.append(os.path.join(root, filename))

#print(rights_files)

arr2 = []

for item in arr:
    if '/' in item:
        item = item.replace('/', '\\')
    arr2.append(item.replace('C:\\torrents_project\\', ''))


print(f'arr2 : {arr2}')


d = dict()
for path in arr2:
    parent = d
    for dir in path.split('\\'):
        if dir not in parent:
#            print(f'parent : {parent}')
            parent[dir] = dict()
        parent = parent[dir]


print(json.dumps(d, indent=4))


def print_dict(dictionary, ident='', braces=0):
    """ Recursively prints nested dictionaries."""
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print('lolilol' + '%s%s%s%s' %(ident,braces*'[',key,braces*']'))
            print_dict(value, ident+'  ', braces+1)
        else:
            print('lalala' + ident+'%s = %s' %(key, value))


print(print_dict(d))

print('loliliolzefrlsdjhfgkljsdhfg\n\n\n')

def iterdict(dir, path):
    for k, v in dir.items():
        path = f'{path}/{k}'
        if type(v) == dict:
            print(path)
            iterdict(v, path)
        else:
            print(v)


print(type(d))
print(iterdict(d, path_to_files))




