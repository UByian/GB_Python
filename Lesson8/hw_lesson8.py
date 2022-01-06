# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def extract(cls, dd_mm_yyyy):
        my_date = []

        for i in dd_mm_yyyy.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.dd_mm_yyyy)}'


today = Data('06 - 01 - 2022')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2022'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))