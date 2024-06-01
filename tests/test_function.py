import pytest

from src.functions import mask_number

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