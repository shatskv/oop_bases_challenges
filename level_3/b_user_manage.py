"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""


class ErrorSendMixin:
    @staticmethod
    def send_error() -> None:
        print("Такого пользователя не существует.")


class UserManager:
    def __init__(self) -> None:
        self.usernames = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames


class AdminManager(UserManager, ErrorSendMixin):
    def ban_username(self, username: str) -> None:
        try:
            self.usernames.remove(username)
        except ValueError:
            self.send_error()


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        self.usernames.clear()


if __name__ == '__main__':
    usernames = ['daro', 'garo', 'malo', 'dera', 'fola']
    print('\nUserManager\n')
    user_manager = UserManager()
    user_manager.usernames = usernames.copy()
    user_manager.add_user('new_user')
    print(user_manager.get_users())
    print('\nAdminManager\n')
    admin_manager = AdminManager()
    admin_manager.usernames = usernames.copy()
    admin_manager.add_user('new_user_2')
    admin_manager.ban_username('malo')
    print(admin_manager.get_users())
    print('\nSuperAdminManager\n')
    super_manager = SuperAdminManager()
    super_manager.usernames = usernames.copy()
    super_manager.add_user('new_user_2')
    super_manager.ban_username('malo')
    super_manager.ban_username('malo222')
    print(super_manager.get_users())
    super_manager.ban_all_users()
    print(super_manager.get_users())
