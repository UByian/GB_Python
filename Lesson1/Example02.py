# password = input("Введите пароль >>>")
#
# original_password = "Correct"
#
# if original_password == password:
#     print("Верно")
# else:
#     print("Неверно")

age = int(input("Введите ваш возраст >>>"))

if age >= 14:
    print("Паспорт можно получить")

    if 20 <= age < 45:
        print("Паспорт можно поменять")
elif age < 1:
    print("Custom")
else:
    print("Паспорт нельзя получить")
