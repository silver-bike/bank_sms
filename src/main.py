import json
from src.functions import mask_number

with open("../operations.json", "r", encoding='utf8') as data_file:
    json_data = data_file.read()
    data = json.loads(json_data)


sms_filter = "EXECUTED"

sms_lst = []

for msg in data:
    if msg:
        sms_id = msg.get('id', '')
        sms_state = msg.get('state', '')
        sms_date_time = msg.get('date', '')
        sms_date = ".".join(sms_date_time.split("T")[0].split("-")[::-1])
        sms_description = msg.get('description', '')
        sms_from = msg.get('from', '')
        sms_to = mask_number(msg.get('to', ''))
        if sms_from:
            sms_from = mask_number(sms_from)
            sms_send = ' -> '
        else:
            sms_send = ''
        sms_amount = msg.get('operationAmount')['amount']
        sms_currency = msg.get('operationAmount')['currency']['name']
        sms_text = (f'{sms_date} {sms_description}\n'
                    f'{sms_from}{sms_send}{sms_to}\n'
                    f'{sms_amount} {sms_currency}\n')
        if sms_filter == sms_state:
            sms_lst.append((sms_date_time, sms_text))

sms_lst.sort(reverse=True)
sms_limit = min(5, len(sms_lst))
for key, sms in sms_lst[:sms_limit]:
    print(sms)
