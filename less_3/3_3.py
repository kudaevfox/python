a = int(input("Введите первый аргумент: "))
b = int(input("Введите второй аргумент: "))
c = int(input("Введите третий аргумент: "))

def my_func(a, b, c):
    summ = 0
    if a > b or a > c:
        summ += a
    if b > a or b > c:
        summ += b
    if c > a or c > b:
        summ += c
    return summ

print(my_func(a, b, c))