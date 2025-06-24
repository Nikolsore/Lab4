user_input = input("Введите ваш возраст: ")
try:
    age = int(user_input)
    if age < 0:
        print("Ошибка! Введите положительное число")
    else:
        if age >= 18:
            print("Вам есть 18+.")
        else:
            print("Вам нет 18+.")
except ValueError:
    print("Ошибка!")
