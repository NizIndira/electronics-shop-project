"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
from pathlib import Path

import pytest

import settings
import src
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


def test_repr(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test_str(item):
    assert str(item) == 'Смартфон'


def test_sum_classes():
    item1 = Item('Чехол', 200, 25)
    item2 = Item('Кабель', 500, 5)
    assert item1 + item2 == 30


def test_exceptions():
    TEST_PATH = Path.joinpath(settings.ROOT_PATH, 'tests')

    src.item.DATA_FILE = 'wrong_file.csv'
    src.item.DATA_PATH = Path.joinpath(settings.SRC_PATH, src.item.DATA_FILE)
    Item.instantiate_from_csv()
