"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        if income < 0:
            return
        self.balance += income

    def decrease_balance(self, income: float):
        if self.balance - income < 0:
            raise ValueError('Недостаточно средств!')
        self.balance -= income


if __name__ == '__main__':
    user_account = BankAccount('Василий Пупкин', 1604)
    print(user_account.balance)
    user_account.decrease_balance(1000)
    print(user_account.balance)
    user_account.decrease_balance(1000)
