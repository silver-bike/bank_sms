from src.functions import print_sms, sms_listing
from j_foo import data_from_json

data = data_from_json("../operations.json")
sms_lst = sms_listing(data)
print_sms(sms_lst, 5)
