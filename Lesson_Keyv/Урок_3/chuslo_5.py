while True:
    print("--- МЕНЮ ---")
    print("1 - Додавання двох чисел")
    print("2 - Віднімання двох чисел")
    print("3 - Ділення двох чисел")
    print("4 - Вихід")

    choice = input("Ваш вибір (1/2/3/4): ")


    if choice == "1":
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print("Результат додавання:", a + b)

    elif choice == "2":
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        print("Результат віднімання:", a - b)

    elif choice == "3":
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        if b == 0:
            print("Помилка: ділення на нуль неможливе!")
        else:
            print("Результат ділення:", a / b)

    elif choice == "4":
        print("Вихід із програми. ")
        break

    else:
        print("Невірний вибір . Спробуйте ще раз.")
