# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
staff_salaries = open('staff_salaries.txt', 'r')
average_salary = 0
i = 0
for idx in staff_salaries:
    worker = idx.split()
    if int(worker[2]) < 20:
        print(worker[0])
    i += 1
    average_salary += int(worker[2])
print(f'Средняя зарплата сотрудников: {average_salary / i} тыс.')
