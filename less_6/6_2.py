# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self, weight, thickness):
        self.weight = weight
        self.thickness = thickness
        print(f'Масса: {self._length * self._width * (self.weight * self.weight)}')

m29 = Road(20, 6)
m29.calculate_mass(5, 5)