import pytest
import csv
from main import Item

class TestItem:

    @pytest.fixture
    def item(self):
        return Item('test', 10, 2)

    @pytest.fixture
    def csv_file(tmp_path):
        # Создаем временный файл CSV и заполняем его данными
        csv_data = [
            {'name': 'item1', 'price': '10.0', 'quantity': '5.0'},
            {'name': 'item2', 'price': '20.0', 'quantity': '3.0'},
            {'name': 'item3', 'price': '30.0', 'quantity': '2.0'}
        ]
        file_path = tmp_path / 'test.csv'
        with open(file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'price', 'quantity'])
            writer.writeheader()
            writer.writerows(csv_data)
        return file_path

    def test_calculate_total_price(self, item):
        assert item.calculate_total_price() == 20

    def test_apply_discount(self, item):
        item.price = item.apply_discount()
        assert item.price == 8.5

    def test_all_items(self, item):
        assert item in Item.all

    def test_discount_rate(self, item):
        assert Item.discount_rate == 0.85

    def test_item_attributes(self, item):
        assert item.name == 'test'
        assert item.price == 10
        assert item.quantity == 2

    def test_instantiate_from_csv_returns_list_of_objects(self, csv_file):
        items = Item.instantiate_from_csv(csv_file)
        assert isinstance(items, list)
        assert all(isinstance(item, Item) for item in items)

    def test_instantiate_from_csv_returns_correct_size(self, csv_file):
        items = Item.instantiate_from_csv(csv_file)
        assert len(items) == 3

    def test_instantiate_from_csv_handles_exception(self, csv_file):
        wrong_format_file = csv_file.parent / 'wrong.csv'
        with open(wrong_format_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'price', 'quantity'])
            writer.writerow(['item1', '10.0', '5.0'])
            writer.writerow(['item2', '20.0', '3.0'])
            writer.writerow(['item3', '30.0'])  # Нет поля "quantity"
        with pytest.raises(Exception):
            Item.instantiate_from_csv(wrong_format_file)

    def test_is_integer_returns_true_for_integers(self):
        # Arrange
        n = 5

        # Act
        result = Item.is_integer(n)

        # Assert
        assert result == True

    def test_is_integer_returns_true_for_floats_that_are_integers(self):
        # Arrange
        n = 5.0

        # Act
        result = Item.is_integer(n)

        # Assert
        assert result == True

    def test_is_integer_returns_false_for_floats_that_are_not_integers(self):
        # Arrange
        n = 5.5

        # Act
        result = Item.is_integer(n)