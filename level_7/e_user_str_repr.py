"""
Задания:
    1. Запустите текущий код и посмотрите на вывод.
    2. Допишите класс User таким образом, чтобы при вызове print() на его инстансах появлялась информация
       об айдишнике пользователя и его емэйле, а при вызове repr() возвращалась информация о том, является ли пользователь
       админом
"""


class User:
    def __init__(self, user_id: int, email: str, is_admin: bool) -> None:
        self.user_id = user_id
        self.email = email
        self.is_admin = is_admin

    def __str__(self) -> str:
        return f'User id: {self.user_id}, email: {self.email}'
    
    def __repr__(self) -> str:
        admin_condition = '' if self.is_admin else ' not'
        return f'User with id {self.user_id} is{admin_condition} admin'


if __name__ == '__main__':
    user_instance = User(user_id=3, email='dev@yandex.ru', is_admin=True)
    print(user_instance)
    print(repr(user_instance))

    user_instance_two = User(user_id=3, email='dev@yandex.ru', is_admin=False)
    print('\n', repr(user_instance_two), sep='')
