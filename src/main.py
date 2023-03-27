import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
        Класс товара, имеющий следующие атрибуты:
        - name: наименование товара
        - price: цена товара
        - quantity: количество товара
        - discount_rate: уровень цен с учетом скидки
        - all: список всех созданных товаров
        """

    discount_rate = 0.85  # уровень цен с учетом скидки
    all = []  # список созданных товаров

    def __init__(self, name, price, quantity):
        """
        Конструктор класса Item, создающий новый экземпляр товара.

        :param name: наименование товара
        :param price: цена товара
        :param quantity: количество товара
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)  # добавляем экземпляр в список созданных товаров

    @classmethod
    def instantiate_from_csv(cls, path: str = 'items.csv') -> list:
        """
        Создает новые экземпляры товаров из CSV-файла.

        :param path: путь к CSV-файлу
        :return: список экземпляров товаров
        """

        try:
            with open(path, 'r', encoding='windows-1251', newline='') as fp:
                data = csv.DictReader(fp)
                required_fields = ['name', 'price', 'quantity']
                for row in data:
                    if all(field in row for field in required_fields):
                        name = row['name']
                        price = int(float(row['price']))
                        quantity = int(float(row['quantity']))
                        try:
                            item = cls(name, price, quantity)
                        except ValueError as e:
                            print(f"Не удалось создать товар {name}: {str(e)}")
                        else:
                            raise InstantiateCSVError('Файл item.csv поврежден')
        except FileNotFoundError:
            raise FileNotFoundError('Отсутствует файл item.csv')
        return cls.all

    @staticmethod
    def is_integer(n: float) -> bool:
        """
        Проверяет, является ли заданное число целым.

        :param n: число, которое нужно проверить
        :return: True, если число целое, иначе False
        """

        return isinstance(n, int) or (isinstance(n, float) and n.is_integer())

    @property
    def name(self) -> str:
        """
        Получает наименование товара.

        :return: наименование товара
        """

        return self.__name

    @name.setter
    def name(self, value: str):
        """
        Устанавливает наименование товара.

        :param value: новое наименование товара
        """

        if len(value) <= 10:
            self.__name = value
        else:
            print('Exception: Длина наименования товара превышает 10 допустимых символов.')

    def calculate_total_price(self) -> float:
        """
        Вычисляет общую стоимость товаров.

        :return: float, общая стоимость товаров.
        """

        return self.price * self.quantity

    def apply_discount(self) -> float:
        """Применить скидку к цене товара и вернуть новую цену.

        Returns:
        float: Цена товара со скидкой.
            """

        return self.discount_rate * self.price

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта товара в формате, который может быть использован для его создания.

        Returns:
        str: Строковое представление объекта товара.
        """
        # Используется форматирование строк, чтобы создать строковое представление товара.

        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """Возвращает строку с названием товара.

        Returns:
        str: Название товара.
        """
        # Возвращает название товара, которое сохранено в атрибуте __name.

        return self.__name


class Phone(Item):
    """
    Класс телефона, наследующий класс товара.
    """

    def __init__(self, name, price, quantity, number_of_sim):
        """
        Конструктор класса Phone, создающий новый экземпляр телефона.

        :param name: наименование телефона
        :param price: цена телефона
        :param quantity: количество телефонов
        :param number_of_sim: количество физических SIM-карт
        """

        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        """
        Получает количество физических SIM-карт.

        :return: количество физических SIM-карт
        """

        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> int:
        """
        Устанавливает количество физических SIM-карт.

        :param value: новое количество физических SIM-карт
        """

        if not self.is_integer(value) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = value

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса Phone.

        :return: строковое представление экземпляра класса Phone
        """

        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self) -> str:
        """
        Возвращает наименование телефона.

        :return: наименование телефона
        """

        return self.name

    def __add__(self, other):
        """
        Определяет операцию сложения экземпляров класса Phone.

        :param other: другой экземпляр класса Phone
        :return: новый экземпляр класса Phone, полученный в результате сложения
        """

        if not isinstance(other, Phone):
            raise TypeError("Нельзя сложить экземпляр класса Phone с объектом другого класса.")
        return type(self)(self.name, self.price, self.quantity + other.quantity, self.number_of_sim)

    def __radd__(self, other):
        """
        Определяет операцию сложения экземпляров класса Phone.

        :param other: другой экземпляр класса Phone
        :return: новый экземпляр класса Phone, полученный в результате сложения
        """

        if not isinstance(other, Phone):
            raise TypeError("Нельзя сложить экземпляр класса Phone с объектом другого класса.")
        return self.__add__(other)


class LanguageMixin:
    """Дополнительный функционал по хранению и изменению раскладки клавиатуры"""

    def __init__(self, language='EN'):
        """Инициализирует атрибут языка."""

        self._language = language

    @property
    def language(self) -> str:
        """str: Возвращает язык."""

        return self._language

    def change_lang(self):
        """Меняет язык между 'EN' и 'RU'."""

        self._language = 'RU' if self._language == 'EN' else 'EN'


class Keyboard(Item, LanguageMixin):
    """Представляет элемент "клавиатура"""

    def __init__(self, name, price, quantity, language='EN'):
        Item.__init__(self, name, price, quantity)
        LanguageMixin.__init__(self, language)

    @property
    def language(self) -> str:
        """str: Возвращает язык клавиатуры."""

        return self._language

    @language.setter
    def language(self, value):
        """Вызывает AttributeError, если меняется атрибут"""
        raise AttributeError("can't set attribute")

    def change_lang(self):
        """Меняет язык клавиатуры между 'EN' и 'RU'."""
        super().change_lang()
