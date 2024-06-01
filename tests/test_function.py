import pytest

from src.functions import mask_number, sms_listing, print_sms

def test_mask_number():
    assert (mask_number('0000000000000000')
            == '0000 00** **** 0000')
    assert (mask_number('0000111122223333')
            == '0000 11** **** 3333')
    assert (mask_number('00000000000000000000')
            == '**0000')
    assert (mask_number('00001111222233334444')
            == '**4444')


def test_mask_wrong_number():
    with pytest.raises(IndexError):
        mask_number("")


def test_sms_listing():
    assert (sms_listing([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                         'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                         'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                         'to': 'Счет 64686473678894779589'}]) ==
                        [('2019-08-26T10:50:58.294041',
                        '26.08.2019 Перевод организации\n'
                        'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                        '31957.58 руб.\n')])


def test_print_sms():
    with pytest.raises(AttributeError):
        print_sms("")