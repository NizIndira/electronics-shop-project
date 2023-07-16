import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone", 120000, 5, 2)


def test_phone_init(phone):
    assert phone.name == 'iPhone'
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_sum_classes():
    item = Item("Смартфон", 10000, 20)
    phone = Phone("iPhone", 120000, 5, 2)
    assert item + phone == 25
