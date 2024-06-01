import json
from src.functions import print_sms, sms_listing

with open("../operations.json", "r", encoding='utf8') as data_file:
    json_data = data_file.read()
    data = json.loads(json_data)


sms_lst = sms_listing(data)

print_sms(sms_lst)
