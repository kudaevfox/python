# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.

class Cage:

    def __init__(self, quantity: int):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Разность меньше 0')

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, cells_in_row):
         row = ''
         for i in range(int(self.quantity / cells_in_row)):
             row += f'{"*" * cells_in_row}\\n '
         row += f'{"*" * (self.quantity % cells_in_row)}'
         return row

a = Cage(10)
b = Cage(20)

print(b.make_order(6))