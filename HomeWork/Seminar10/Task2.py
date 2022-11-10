"""Задание 2 Создать метакласс для паттерна Синглтон (см. конец вебинара)"""
class MyMetaClass(type):
    obj = None
    #Должен вернуть словарь для атрибутов класса
    @classmethod
    def __prepare__(metacls, name, bases):
        print('Перегружаю __prepare__')
        return type.__prepare__(metacls, name, bases)
    # Должен создать и вернуть новый класс
    def __new__(cls, name, bases, dct):

        first_name = ''
        if first_name == '':
            first_name = name
        else:
            name = first_name
        print(f'Выделение памяти для {name}, '
              f'имеющего кортеж базовых классов {bases} '
              f'и словарь атрибутов {dct}')
        return type.__new__(cls, name, bases, dct)
    #Должен инициализировать созданный класс
    def __init__(cls, name, bases, dct):
        print(f'Инициализация класса {name}')
        
        super(MyMetaClass, cls).__init__(name, bases, dct)
    #Должен создать и вернуть экземпляр нового класса
    def __call__(self, *args, **kwargs):
        print('Перегружаю __call__')

        if self.obj == None:
            self.obj = type.__call__(self, *args, **kwargs)
            return self.obj
        else:
            return self.obj

class P_1():
    pass
class P_2():
    pass

class MyClass(P_1, P_2, metaclass = MyMetaClass):
    atr = 30

a = MyClass()
b = MyClass()
print(a is b)
