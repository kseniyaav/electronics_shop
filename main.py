class Item:
    discount_rate = 0.85 # уровень цен с учетом скидки
    all = []  # список созданных товаров


    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.__class__.all.append(self)  # добавляем экземпляр в список созданных товаров

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.__class__.discount_rate