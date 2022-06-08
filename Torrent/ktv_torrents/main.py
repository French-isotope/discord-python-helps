import os
import json

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
            
            it.path
            listdirs(it)

listdirs(path_to_files)


