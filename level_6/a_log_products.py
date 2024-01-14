"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""


class PrintLoggerMixin:
    @staticmethod
    def log(*message):
        print(*message)


class Product(PrintLoggerMixin):
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price
        self.log(self, 'init instance')

    def get_info(self) -> str:
        info = f'Product {self.title} with price {self.price}'
        self.log('get_info:', info)
        return info


class PremiumProduct(Product, PrintLoggerMixin):
    def increase_price(self) -> None:
        self.price *= 1.2
        self.log('increase_price:', self.price)

    def get_info(self) -> str:
        base_info = super().get_info()
        info = f'{base_info} (Premium)'
        self.log('get_info:', info)
        return f'{base_info} (Premium)'


class DiscountedProduct(Product, PrintLoggerMixin):
    def decrease_price(self) -> None:
        self.price /= 1.2
        self.log('decrease_price:', self.price)

    def get_info(self) -> str:
        base_info = super().get_info()
        info = f'{base_info} (Discounted)'
        self.log('get_info:', info)
        return info


if __name__ == '__main__':
    print('Product:\n')
    product = Product('Утюг', 2500)
    print(product.get_info())

    print('PremiumProduct:\n')
    product_two = PremiumProduct('Чайник', 1500)
    product_two.increase_price()
    print(product_two.get_info())

    print('DiscountedProduct:\n')
    product_three = DiscountedProduct('Стол', 2000)
    product_three.decrease_price()
    print(product_three.get_info())
