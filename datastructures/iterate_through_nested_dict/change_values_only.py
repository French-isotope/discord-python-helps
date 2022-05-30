import json

keys_file = 'dict_keys.json'
values_file = 'dict_vals.json'


with open(keys_file,'r',encoding = 'utf-8') as f1:
    key_ref = json.load(f1)

with open(values_file,'r',encoding = 'utf-8') as f2:
    value_ref = json.load(f2)


"""
def nested_dict_pairs_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all key-value pairs of dict argument
    for key, value in dict_obj.items():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for pair in  nested_dict_pairs_iterator(value):
                yield (key, *pair)
        else:
            # If value is not dict type then yield the value
            yield (key, value)

"""


def nested_dict_pairs_iterator(dict_obj):
    ''' This function accepts a nested dictionary as argument
        and iterate over all values of nested dictionaries
    '''
    # Iterate over all key-value pairs of dict argument
    for key, value in dict_obj.items():
        # Check if value is of dict type
        if isinstance(value, dict):
            # If value is dict then iterate over all its values
            for pair in  nested_dict_pairs_iterator(value):
                yield (key, *pair)
        else:
            # If value is not dict type then yield the value
            yield (key, value)


# Get all key-value pairs of a nested dictionary as list
all_pairs = list(nested_dict_pairs_iterator(key_ref))
for pair in all_pairs:
    print(pair)


with open('test.json','w',encoding = 'utf-8') as f1:
    output_prettified = json.dumps(all_pairs, indent=4, sort_keys=True)
    f1.write(output_prettified)


#print(key_ref)