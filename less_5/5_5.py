# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел
# в файле и выводить ее на экран.
import random
import functools as ft
numbers_file = open('numbers.txt', 'r+')

for idx in range(int(input('Введите колличество случайных чисел: ')) + 1):
    numbers_file.write(f'{(random.randint(10, 100))} ')

content = numbers_file.readline()
print(ft.reduce(lambda acc, x: acc + x, map(int, content.split())))
numbers_file.close()