user = input("Введите число: ")
try:
    num = int(user)
    if num > 0:
        if num % 2 == 0:
            print(f"Число {num} является четным")
        else:
            print(f"Число {num} не является четным")
    else:
        print("Ошибка: число должно быть положительным")
except ValueError:
    print("Ошибка")
