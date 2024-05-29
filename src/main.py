import json

with open("../operations.json", "r", encoding='utf8') as data_file:
    json_data = data_file.read()
    data = json.loads(json_data)


def date_formater(data_date):
    transaction_date = data_date.split('T')[0]
    return '.'.join(transaction_date.split('-')[::-1])


formated_date = date_formater(data[0]['date'])
print(formated_date)