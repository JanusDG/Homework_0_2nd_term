import json
from dict_atd import Dictionary, Node

def into_atd(py_dict):
    our_dict = Dictionary()
    for key,value in py_dict.items():
        if isinstance(value, dict):
            our_dict[key] = into_atd(value)
        elif isinstance(value, list):
            our_dict[key] = [into_atd(item) for item in value]
        else:
            our_dict[key] = value

    return our_dict
