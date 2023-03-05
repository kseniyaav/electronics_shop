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

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not self.is_integer(value) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise TypeError("Нельзя сложить экземпляр класса Phone с объектом другого класса.")
        if type(self) != type(other):
            raise TypeError("Нельзя сложить экземпляры разных классов.")
        return type(self)(self.name, self.price, self.quantity + other.quantity, self.number_of_sim)

    def __radd__(self, other):
        return self.__add__(other)
