import pytest
from ..sou import  my_functions

def test_add():
    result = my_functions.add(1,2)
    assert result == 5

def test_divide():
    result = my_functions.divide(4,0)
    assert result == 0

def test_sorting():
    result = my_functions.sortting([5,2,3,'4'])
    assert result == [2,3,4,5]