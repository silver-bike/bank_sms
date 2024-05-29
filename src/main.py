import json

with open("../operations.json", "r", encoding='utf8') as data_file:
    json_data = data_file.read()
    data = json.loads(json_data)


for msg in data:
    if msg:
        date_sms = msg.get('date', '')
        descr_sms = msg.get('description', '')
        sender_sms = msg.get('from', '')
        address_sms = msg.get('to', '')
        if sender_sms:
            sign_sms = ' -> '
        else:
            sign_sms = ''
        money_sms =msg.get('operationAmount')['amount']
        currency_sms = msg.get('operationAmount')['currency']['name']
        print(f'{date_sms} {descr_sms}\n{sender_sms}{sign_sms}{address_sms}\n{money_sms} {currency_sms}\n')


