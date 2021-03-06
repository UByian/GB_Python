# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_f = open('test.txt', 'w')
line = input('Введите текст \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст \n')
    if not line:
        break

my_f.close()
my_f = open('test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

def count_info():
    try:
        with open('file2.txt', 'r', encoding="utf-8") as file:
            my_list = file.readlines()
            for i in range(len(my_list)):
                new_l = my_list[i].split()
                print(f'Количество строк в файле {len(my_list)}.')
                print(f'В {i + 1}-ой строке {len(new_l)} слов(а)')
    except FileNotFoundError:
        return 'Файл не найден.'


count_info()

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('file3_salary.txt', 'r', encoding="utf-8") as file:
    sal = []
    poor = []
    my_list = file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
    print(f'Оклад менее 20 тыс. {poor}, средний доход {sum(map(float, sal)) / len(sal)}')

# 4. Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file4.txt', 'r', encoding="utf-8") as file_num:
    for i in file_num:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('file4_new.txt', 'w', encoding="utf-8") as file_num_2:
    file_num_2.writelines(new_file)


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def write_summ():
    try:
        with open('file5.txt', 'w+') as f_summ:
            line = input('Введите набор чисел, разделенных пробелами: ')
            f_summ.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно введен номер')
    except FileNotFoundError:
        return 'Файл не найден.'


write_summ()


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

def count_subjects():
    try:
        subj = {}
        with open('file6.txt', 'r', encoding="utf-8") as lesson:
            for line in lesson:
                name, subject = line.split(':')
                sum_subj = sum(map(int, ''.join([i for i in subject if i == ' ' or ('0' <= i <= '9')]).split()))
                subj[name] = sum_subj
                print(f"{subj}")
    except FileNotFoundError:
        return 'Файл не найден.'


count_subjects()

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

import json
margin = {}
mr = {}
marg = 0
marg_aver = 0
i = 0
with open('file7.txt', 'r') as f_file:
    for line in f_file:
        name, firm, earnings, expenses = line.split()
        margin[name] = int(earnings) - int(expenses)
        if margin.setdefault(name) >= 0:
            marg = marg + margin.setdefault(name)
            i += 1
    if i != 0:
        marg_aver = marg / i
        print(f'Прибыль средняя - {marg_aver:.2f}')
    else:
        print(f'Убыток у всех')
    mr = {'Средняя прибыль': round(marg_aver)}
    margin.update(mr)
    print(f'Прибыль каждой компании - {margin}')

with open('file7.json', 'w') as write_js:
    json.dump(margin, write_js)

    js_str = json.dumps(margin)
    print(f'Создан json-объект: \n '
          f' {js_str}')

