import pytest

from main import Item

class TestItem:

    @pytest.fixture
    def item(self):
        return Item('test', 10, 2)

    def test_calculate_total_price(self, item):
        assert item.calculate_total_price() == 20

    def test_apply_discount(self, item):
        item.apply_discount()
        assert item.price == 8.5

    def test_all_items(self, item):
        assert item in Item.all

    def test_discount_rate(self, item):
        assert Item.discount_rate == 0.85

    def test_item_attributes(self, item):
        assert item.name == 'test'
        assert item.price == 10
        assert item.quantity == 2