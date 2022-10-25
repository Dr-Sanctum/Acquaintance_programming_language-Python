"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h,
соответственно.Для определения расхода ткани по каждому типу одежды
использовать формулы: для пальто (v/6.5 + 0.5),для костюма (2*h + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""
from abc import ABC, abstractmethod


class AbstractClothes(ABC):

    @abstractmethod
    def cloth_expenditure(self):
        pass


class Clothes(AbstractClothes):

    def __init__(self, coat_v: float, suit_h: float):
        self.coat = coat_v
        self.suit = suit_h

    @property
    def cloth_expenditure(self):
        expenditure_coat = round(self.coat / 6.5 + 0.5, 2)
        expenditure_suit = round(2 * self.suit + 0.3, 2)
        print(f'Расход ткани на пальто = {expenditure_coat}')
        print(f'Расход ткани на костюм = {expenditure_suit}')
        print(f'Расход всего = {round(expenditure_coat + expenditure_suit, 2)}')

a = Clothes(4.24,5.134)
a.cloth_expenditure
