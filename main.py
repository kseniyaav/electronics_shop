import csv

class Item:
    discount_rate = 0.85 # уровень цен с учетом скидки
    all = []  # список созданных товаров


    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)  # добавляем экземпляр в список созданных товаров

    @classmethod
    def instantiate_from_csv(cls, path):
        """Создаёт новые экзэмпляры из csv файла"""
        with open(path, 'r', encoding='windows-1251', newline='') as fp:
            data = csv.DictReader(fp)
            for row in data:
                name = row['name']
                price = int(float(row['price']))
                quantity = int(float(row['quantity']))
                try:
                    item = cls(name, price, quantity)
                except ValueError as e:
                    print(f"Не удалось создать товар {name}: {str(e)}")
            return cls.all

    @staticmethod
    def is_integer(n):
        return isinstance(n, int) or (isinstance(n, float) and n.is_integer())

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) <= 10:
            self.__name = value
        else:
            print('Exception: Длина наименования товара превышает 10 допустимых символов.')

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        return self.discount_rate * self.price
