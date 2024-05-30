import json

with open("../operations.json", "r", encoding='utf8') as data_file:
    json_data = data_file.read()
    data = json.loads(json_data)

sms_filter = "EXECUTED"


def read_number(some_number):
    number_lst = some_number.split()
    num = list(number_lst[-1])
    if len(num) == 16:
        num[6:12] = ["*","*"," ","*","*","*","*"," ",]
        num.insert(4, " ")
    else:
        num = num[-4:]
        num.insert(0, "*")
        num.insert(0, "*")
    number_lst[-1] = ''.join(num)
    return ' '.join(number_lst)


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
            print(f'{sms_date} {sms_description}\n{sms_from}{sms_send}{read_number(sms_to)}\n{sms_amount} {sms_currency}\n')
            print(read_number(sms_to))