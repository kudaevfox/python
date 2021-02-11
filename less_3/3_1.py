a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

def devide_number(a, b):
    if a != 0 and b != 0:
        return a / b
    else:
        return "Ошибка"

print(devide_number(a,b))