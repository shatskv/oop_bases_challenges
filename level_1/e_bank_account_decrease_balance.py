"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> None:
        self.balance += income
        self.balance = round(self.balance, 2)

    def decrease_balance(self, income: float) -> None:
        if self.balance - income < 0:
            raise ValueError('Недостаточно средств!')
        self.balance -= income
        self.balance = round(self.balance, 2)


if __name__ == '__main__':
    user_account = BankAccount('Василий Пупкин', 1604)
    print(user_account.balance)
    user_account.balance = 0.2
    user_account.increase_balance(0.1)
    print(user_account.balance)
    user_account.balance = 1604
    print(user_account.balance)
    user_account.decrease_balance(1000)
    print(user_account.balance)
    user_account.decrease_balance(1000)
