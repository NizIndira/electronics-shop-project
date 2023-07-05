"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv

import pytest

from settings import PATH_CSV_ITEMS
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_item_init(item):
    assert item.name == "Смартфон"
    assert item.price == 10_000
    assert item.quantity == 20
    assert Item.all == [item]


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200_000


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10_000

def test_name():
    item1 = Item('Смартфон', 1000, 1)

    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'

def test_instantiate_from_csv():
    with open(PATH_CSV_ITEMS) as file:
        data = csv.DictReader(file)
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert len(Item.all) == 5
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
