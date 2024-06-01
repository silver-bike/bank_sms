import json


def data_from_json(file):
    with open(file, "r", encoding='utf8') as data_file:
        json_data = data_file.read()
        data = json.loads(json_data)
        return data
