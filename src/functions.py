def mask_number(some_number):
    number_lst = some_number.split()
    num = list(number_lst[-1])
    if len(num) == 16:
        num[6:12] = ["*", "*", " ", "*", "*", "*", "*", " "]
        num.insert(4, " ")
    else:
        num = num[-4:]
        num.insert(0, "*")
        num.insert(0, "*")
    number_lst[-1] = ''.join(num)
    return ' '.join(number_lst)


def sms_listing(some_data, sms_filter="EXECUTED"):
    sms_lst = []
    for msg in some_data:
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
    return sms_lst


def print_sms(some_list, some_limit=5):
    some_list.sort(reverse=True)
    sms_limit = min(some_limit, len(some_list))
    for key, sms in some_list[:sms_limit]:
        print(sms)