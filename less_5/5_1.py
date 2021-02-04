# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные,
# вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
new_file = open('new_file.txt', 'w')

while True:
    print('Введите текст. Для выхода нажмите Enter: ')
    string_input = input()
    if string_input != '':
        new_file.write(f'{string_input}\n')
    else:
        break

new_file.close()
