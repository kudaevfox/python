# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.
read_file = open('new_file.txt', 'r')

sum_string = 0
for line in read_file:
    sum_string += 1
    print(f'В {sum_string} строке {len(line.split())} слов(а)')
