# Задание 1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

to_int = 7
to_float = 11.9
to_str = "Всем привет!"
to_list = ['a', '5']
to_tuple = ('b', '7')
to_dict = {'city': 'Moscow', 'country': 'Russia'}

my_list = [to_int, to_float, to_str, to_list, to_tuple, to_dict]
for i in my_list:
    print(f'{i} is {type(i)}')

# Задание 2: Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

el_count = int(input("Количество элементов списка "))
my_list = []
i = 0
element = 0
while i < el_count:
    my_list.append(input("Значение списка "))
    i += 1

for elem in range(int(len(my_list) / 2)):
    my_list[element], my_list[element + 1] = my_list[element + 1], my_list[element]
    element += 2
print(my_list)

# Задание 3: Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = int(input("Введите номер месяца: "))
if month == 12 or month == 1 or month == 2:
    print(seasons_dict.get(1))
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

# Задание 4: Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_string = input("Введите предложение: ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word[element]}")
        number += 1
    else:
        print(f" {number} {my_word[(element)][0:10]}")
        number += 1

# Задание 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [9, 7, 5, 4, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите рейтинг: "))
while digit != 000:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Текущий список - {my_list}")
    digit = int(input("Введите рейтинг "))

