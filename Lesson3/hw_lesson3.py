# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division():
    try:
        a = int(input("Введите делимое: "))
        b = int(input("Введите делитель: "))
        result = a / b
    except ZeroDivisionError:
        return "Деление на ноль невозможно!"
    return result
print("Результат деления: ",  division())

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(name, lastname, year_of_birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {year_of_birth} Город проживания: {city} Email: {email} Телефон: {phone}')


user_info(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    year_of_birth=input('Год Рождения: '),
    city=input('Город проживания: '),
    email=input('email: '),
    phone=input('phone: ')
)

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    if x >= z and y >= z:
        return x + y
    elif x > y and x < z:
        return x + z
    else:
        return y + z
print(f'Результат = {my_func(int(input("Введите первое число: ")), int(input("Введите второе число: ")), int(input("Введите третье число: ")))}')


