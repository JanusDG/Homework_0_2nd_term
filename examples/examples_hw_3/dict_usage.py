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

def json_view(value, depth=1, key = None):
    rez = ""
    if isinstance(value, Dictionary):
        if key is not None:
            rez += "   " * depth + key + ": " + '\n'

        rez += "   " * depth + "{" + '\n'
        for key, value in value.items:
            rez += json_view(value, depth + 1, key=key)
        rez = rez[:-2]
        rez += "\n"
        rez += "   " * depth + "}" + "\n"
    elif isinstance(value, list):
        if key is not None:
            rez += "   " * depth + key + ": " + '\n'
        rez += "   " * depth + "[" + "\n"
        for item in value:
            rez += json_view(item, depth + 1)[:-1] + ','  + "\n"
        rez = rez[:-2]
        rez += "\n"
        rez += "   " * depth + "]" + "\n"
        rez += "   " * depth + "]" + "\n"
    else:
        rez += "   " * depth + str(key) + ": " + str(value) + ","
        rez += "\n"
    return rez 

if __name__ == "__main__":
    with open("data.json", "r") as file:
        py_dict = json.load(file)
    print(json_view(into_atd(py_dict)))
    
