class NonNegative:
    """Этот класс поможет нам сделать атрибуты дескриптора"""
    #новый питон
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        #instance - экземпляр нужного класса 
        # value присваемое значение
        if value< 0:
            raise ValueError ('Не может быть отрицательным')
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]
        
class OnlyNumber:
    """Этот класс поможет нам сделать атрибуты дескриптора"""
    #новый питон
    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value: str):
        #instance - экземпляр нужного класса 
        # value присваемое значение
        if not value.isdigit():
            raise ValueError ('Должно быть положительным числом')
        instance.__dict__[self.my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self.my_attr]

class Road:
    _lenght = NonNegative()
    _width = NonNegative()

    def __init__(self,lenght: int,width: int):
        self._lenght = lenght
        self._width = width

    mass_square_meter = 25
    thickness = 0.05

    def mass(self):
        result = self._lenght * self._width * self.mass_square_meter * self.thickness
        print(f'Масса асфальта для параметров дороги: \n \
            Длина = {self._lenght} м\n \
            Ширина = {self._width} м\n \
            Масса квадратного метра толщиной 1см = {self.mass_square_meter} кг\n \
            При толщине полотна = {self.thickness} м\n \
            Равна {result} кг или {result/1000} т.')

class MyClass:
    number_string = OnlyNumber()
    def __init__(self, stringOnlyNumber: str):
        self.number_string = stringOnlyNumber
    def string_to_number(self):
        return int(self.number_string)

#Проверка первого дескриптора
# a = Road(20,-5000)
# a.mass()

#Проверка Второго дескриптора
b = MyClass('рп345')
print(b.number_string)
