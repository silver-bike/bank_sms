import json

with open("../operations.json", "r", encoding='utf8') as data_file:
    json_data = data_file.read()
    data = json.loads(json_data)


sms_filter = "EXECUTED"

for msg in data:
    if msg:
        sms_id = msg.get('id', '')
        sms_state = msg.get('state', '')
        sms_date_time = msg.get('date', '')
        sms_date = ".".join(sms_date_time.split("T")[0].split("-")[::-1])
        sms_description = msg.get('description', '')
        sms_from = msg.get('from', '')
        sms_to = msg.get('to', '')
        if sms_from:
            sms_send = ' -> '
        else:
            sms_send = ''
        sms_amount = msg.get('operationAmount')['amount']
        sms_currency = msg.get('operationAmount')['currency']['name']
        if sms_filter == sms_state:
            print(f'{sms_date} {sms_description}\n{sms_from}{sms_send}{sms_to}\n{sms_amount} {sms_currency}\n')
