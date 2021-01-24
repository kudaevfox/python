x = int(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))


def my_func(x, y):
    sqr_number = x ** y
    return sqr_number

def my_func_cicle(x, y):
    sqr_number = x
    i = 1
    for i in range((y*-1)+1):
        sqr_number /= x
        i += 1
    return sqr_number

print(my_func(x, y))
print(my_func_cicle(x, y))