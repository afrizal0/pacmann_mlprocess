
from src.utils.utils import *

def test_is_even_with_even():
    param = 2
    expected = True
    actual = is_even(param)

    assert expected == actual

def test_is_even_with_odd():
    param = 3
    expected = False 
    actual = is_even(param)

    assert expected == actual

