import pytest
import csv
from src.main import Phone, Item

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120000, 5, 2)

def test_phone_init(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test_phone_set_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
    with pytest.raises(ValueError):
        phone.number_of_sim = 0.5
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3

def test_phone_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_phone_str(phone):
    assert str(phone) == "iPhone 14"

def test_phone_add(phone):
    with pytest.raises(TypeError):
        phone + 1
    with pytest.raises(TypeError):
        phone + "iPhone 14"
    with pytest.raises(TypeError):
        phone + Item("Samsung Galaxy S22", 100000, 3)
    result = phone + Phone("iPhone 14", 120000, 2, 2)
    assert result.name == "iPhone 14"
    assert result.price == 120000
    assert result.quantity == 7
    assert result.number_of_sim == 2


def test_phone_radd(phone):
    result = Phone("iPhone 14", 120000, 2, 2).__add__(phone)
    assert result.name == "iPhone 14"
    assert result.price == 120000
    assert result.quantity == 7
    assert result.number_of_sim == 2




