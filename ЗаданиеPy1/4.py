while True:
    user_input = input("Введите число: ")
    if user_input == "exit":
        print("Выход из программы...")
        break
    
    stripped = user_input.lstrip('-')
    if stripped.isdigit() and stripped != '' and (len(user_input) - len(stripped)) <= 1:
        print(f"В этом числе {len(stripped)} цифр.")
    else:
        print("Ошибка: данные не являются числом.")
