# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

translate_file = open('translate.txt', 'r')
success_translate = open('success_translate.txt', 'w')
translate_list = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
for idx in translate_file:
    temp_string = idx.split()
    temp_string.insert(1, translate_list[temp_string[0]])
    del temp_string[0]
    success_translate.write(f'{" ".join(temp_string)}\n')
success_translate.close()
