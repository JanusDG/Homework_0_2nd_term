import json
import requests
from modules.dict_atd import Dictionary, Node

def json_to_dict(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        result = json.load(f)
    return into_atd(result)

def get_data_from_URL(url):
    """(str) -> dict
    Function for getting data from URL (DEEZER)
    """
    querystring = {"q": "eminem"}
    headers = {
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
        'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)
    received_file = json.loads(response.text)
    return into_atd(received_file)


def into_atd(py_dict):
    our_dict = Dictionary()
    for key,value in py_dict.items():
        if isinstance(value, dict):
            our_dict[key] = into_atd(value)
        elif isinstance(value, list):
            our_dict[key] = value
        else:
            our_dict[key] = value

    return our_dict

def in_file(path, data):
    with open(path, "w", encoding= 'utf-8') as f:
        f.write(str(data))
    print('Data is in file', path)

