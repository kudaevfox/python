# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothing:

    def __init__(self, name: str, growth, size):
        self.name = name

class Coat(Clothing):

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    @property
    def square(self):
        return self.size / 6.5 + 0.5

class Costume(Clothing):

    def __init__(self, name: str, growth: int):
        self.name = name
        self.growth = growth

    @property
    def square(self):
        return 2 * self.growth + 0.3


a = Coat('DG', 32)

b = Costume('LV', 31)

print(round(a.square + b.square, 2))