import json
from src.functions import mask_number, sms_listing

with open("../operations.json", "r", encoding='utf8') as data_file:
    json_data = data_file.read()
    data = json.loads(json_data)


sms_lst = sms_listing(data, "EXECUTED")

sms_lst.sort(reverse=True)
sms_limit = min(5, len(sms_lst))
for key, sms in sms_lst[:sms_limit]:
    print(sms)