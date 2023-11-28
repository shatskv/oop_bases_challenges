"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, price: int, weight: float) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    @property
    def full_info(self) -> str:
        return f"Информация о продукте: {self.name}, {self.description}, {self.price}, {self.weight}"


if __name__ == '__main__':
    product = Product('Утюг', 'Утюг на 2000 ВТ', 3000, 2.5)
    print(product.full_info)
