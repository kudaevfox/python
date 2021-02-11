# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
import numpy as np
import functools as ft
class Matrix:

    def __init__(self, matrix):

        self.matrix = matrix

    def __str__(self):

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))



    def __add__(self, other):
        return np.matrix(self.matrix) + np.matrix(other.matrix)


a = Matrix([[2, 2, 3],
           [2, 3, 1],
           [3, 1, 2]])

b = Matrix([[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]])

print(str(a))
