count = int(input("Введите количество элементов списка: "))
list = []
i = 0
j = 0
while i < count:
    list.append(input("Введите значение элемента: "))
    i += 1

for elem in range(int(len(list) / 2)):
    list[j], list[j + 1] = list[j + 1], list[j]
    j += 2
print(list)
