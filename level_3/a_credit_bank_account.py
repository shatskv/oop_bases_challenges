"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float):
        self.balance += amount

    def decrease_balance(self, amount: float):
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self):
        return self.balance > 1000


if __name__ == '__main__':
    bank_account = BankAccount('Петров', 1200)
    bank_account.increase_balance(300)
    bank_account.decrease_balance(200)
    print(f'Person balance: {bank_account.balance}')
    credit_account = CreditAccount('Петров', 1200)
    credit_account.increase_balance(300)
    credit_account.decrease_balance(200)
    print(f'Person credit balance: {credit_account.balance}')
    print(f'This person could have credit: {credit_account.is_eligible_for_credit()}')
    credit_account.decrease_balance(600)
    print(f'Person credit balance: {credit_account.balance}')
    print(f'This person could have credit: {credit_account.is_eligible_for_credit()}')
