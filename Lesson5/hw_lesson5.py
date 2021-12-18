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


# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

    my_file = open('file2.txt', 'r')
    content = my_file.read()
    print(f'Содержимое файла: \n {content}')
    my_file = open('file2.txt', 'r')
    content = my_file.readlines()
    print(f'Количество строк в файле - {len(content)}')
    my_file = open('file2.txt', 'r')
    content = my_file.readlines()
    for i in range(len(content)):
        print(f'Окличество символов {i + 1} - ой строки {len(content[i])}')
    my_file = open('file2.txt', 'r')
    content = my_file.read()
    content = content.split()
    print(f'Общее количество слов - {len(content)}')
