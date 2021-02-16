# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету
# и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re
import functools

with open('task_6.txt', 'r') as task:
    lessons_txt = task.readlines()
lessons = {}
for lesson in lessons_txt:
    find_name = re.findall(r'^\w+', lesson)
    print(find_name)
    find_number = re.findall(r'\d+', lesson)
    sum_hour = functools.reduce(lambda acc, x: acc + x, map(int, find_number))
    lessons[f'{find_name[0]}'] = sum_hour
print(lessons)
