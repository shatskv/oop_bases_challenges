"""
У нас есть класс Product, который содержит в себе информацию о продукте.
Еще у нас есть класс AlcoholProduct, но метод is_available для него не подходит, так как
алкоголь нельзя продавать с 5 утра до 11 вечера

Задания:
    1. Переопределите метод is_available в классе AlcoholProduct с использованием super()
    2. is_available у AlcoholProduct должен возвращать False если сейчас часы между 5 утра и 11 вечера.
       Для определения текущего часа можно использовать datetime.now().hour
    3. Создайте экземпляр класса AlcoholProduct и проверьте, можно ли сейчас продавать алкоголь.
"""
from datetime import datetime


class Product:
    def __init__(self, title, price, stock_quantity):
        self.title = title
        self.price = price
        self.stock_quantity = stock_quantity

    def get_discounted_price(self, discount_percentage):
        return self.price * (1 - discount_percentage / 100)

    def is_available(self):
        return self.stock_quantity > 0


class AlcoholProduct(Product):
    available_between = [5, 23]

    def is_available(self):
        hour_now = datetime.now().hour
        return super().is_available() and hour_now > self.available_between[0] and hour_now < self.available_between[1]


if __name__ == '__main__':
    product_data = {'title': 'Водка', 'price': 260, "stock_quantity": 10}
    discount = 20
    product = Product(**product_data)
    print('\nProduct\n')
    print(product.get_discounted_price(discount))
    print(product.is_available())
    product = AlcoholProduct(**product_data)
    print('\nAlcoholProduct\n')
    print(product.get_discounted_price(discount))
    print(product.is_available())
