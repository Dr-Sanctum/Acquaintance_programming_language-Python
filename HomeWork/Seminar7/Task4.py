"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed = 0
    max_speed = 60
    color = 'red'
    name = 'Mazda'
    is_police = False

    def __str__(self) -> str:
        return f'Цвет - {self.color} \nМарка - {self.name} \nРазыскивается? - {"да" if self.is_police else "нет"}'

    def go(self, speed_go:int):
        print('Поехали')
        self.speed = speed_go if speed_go < self.max_speed else self.max_speed

    def stop(self):
        print('Остановились')
        self.speed = 0

    def turn(self, direction):
        print(f'Повернули {direction}')

    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')


class TownCar(Car):
    speed_limit = 60
    max_speed = 80

    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')
        if self.speed > self.speed_limit:
            print(f'Разрешённая скорость в {self.speed_limit} км/ч, превышена')
            self.is_police = True


class SportCar(Car):
    max_speed = 250


class WorkCar(Car):
    speed_limit = 40
    max_speed = 65

    def show_speed(self):
        print(f'Текущая скорость = {self.speed} км/ч')
        if self.speed > self.speed_limit:
            print(f'Разрешённая скорость в {self.speed_limit} км/ч превышена')
            self.is_police = True


class PoliceCar(Car):
    max_speed = 200

a = WorkCar()
a.name = 'Loader'
a.color = 'black'
a.go(50)
a.show_speed()
print(a)

b = SportCar()
b.name = "Maseratti"
b.go(300)
b.show_speed()
b.turn("Направо")
b.stop()
b.show_speed()
print(b)

