#  Создать (не программно) текстовый файл,
#  в котором каждая строка должна содержать данные о фирме:
#  название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки,
# в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
import json
with open('task_7.txt', 'r') as tf:
    task_file = tf.readlines()
firms = {}
average = {}
x = 0
average_profit = 0
for firm in task_file:
    name, type_firm, rev, cost = firm.split()
    if int(rev) > int(cost):
        x += 1
        average_profit += int(rev) - int(cost)
    firms[name] = int(rev) - int(cost)

average["average_profit"] = average_profit // x
final_dict = [firms, average]
out_f = open("task_7.json", "w")
out_f.write(json.dumps(final_dict))
print(json.dumps(final_dict))
