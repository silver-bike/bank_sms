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