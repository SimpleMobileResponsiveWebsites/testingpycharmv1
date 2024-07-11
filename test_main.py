import pytest
from main import add_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(100, 200) == 300

def test_add_numbers_with_negative():
    assert add_numbers(-5, -7) == -12

def test_add_numbers_with_zero():
    assert add_numbers(10, 0) == 10
    assert add_numbers(0, 20) == 20
