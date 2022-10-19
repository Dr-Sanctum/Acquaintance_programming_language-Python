"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""

class Worker:
    name = 'Вася'
    surname = 'Пупкин'
    position = 'Генеральный директор'
    _income = {'wage': 1000, 'bonus':1.9}

class Position(Worker):
    def __str__(self):
        return f'Имя и фамилия: {self.name} {self.surname}, доход = {self._income["wage"] * self._income["bonus"]}'

    def get_full_name(self):
        return f'{self.name} {self.surname}'
        
    def get_total_income(self):
        return (self._income['wage'] * self._income['bonus'])

a = Position()

print(a.get_full_name())
print(a.get_total_income())
print(a)

a.name = 'Петя'
a.surname = 'Васечкин'
print(a)
