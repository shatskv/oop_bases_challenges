"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса ItDepartmentEmployee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self) -> str:
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(self, name: str, surname: str, age: int, salary: float) -> None:
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float) -> None:
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float) -> None:
        employee.salary -= amount


class Developer(ItDepartmentEmployee, SuperAdminMixin):
    def __init__(self, name: str, surname: str, age: int, salary: float, language: str) -> None:
        super().__init__(name, surname, age, salary)
        self.language = language

    def get_info(self) -> str:
        info = super().get_info()
        language = self.language
        return f'{info} language: {language}'


if __name__ == '__main__':
    developer = Developer('Вася', 'Пупкин', 48, 2000, 'Delphi')
    print(developer.get_info())
    developer.increase_salary(developer, 200)
    print(developer.salary)
    developer.decrease_salary(developer, 300)
    print(developer.salary)
