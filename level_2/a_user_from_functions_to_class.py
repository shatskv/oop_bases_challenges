""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""


class User:
    def __init__(self, username: str, user_id: int, name: str) -> None:
        self.username = username
        self.user_id = user_id
        self.name = name
    
    @property
    def capitalized(self) -> str:
        return self.username.capitalize() 
    
    @property
    def description(self) -> str:
        return f'{self.user_id} has {self.username} username and {self.name} name'
