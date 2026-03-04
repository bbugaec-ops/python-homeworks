def main():
    # 1. Отримуємо список чисел від користувача
    raw = input("Введіть числа через пробіл: ")
    try:
        numbers = []
        for x in raw.split():
            numbers.append(float(x))

    except ValueError:
        print("Помилка: потрібно вводити тільки числа.")
        return

    if not numbers:
        print("Список порожній. Немає з чим працювати.")
        return

    while True:
        print("\nМЕНЮ:")
        print("1 – Відобразити список")
        print("2 – Максимальне значення у списку")
        print("3 – Мінімальне значення у списку")
        print("4 – Відобразити елемент за індексом")
        print("5 – Видалити елемент за індексом")
        print("0 – Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print("Список:", numbers)

        elif choice == "2":
            print("Максимальне значення:", max(numbers))

        elif choice == "3":
            print("Мінімальне значення:", min(numbers))

        elif choice == "4":
            try:
                idx = int(input("Введіть індекс елемента: "))
                print(f"Елемент за індексом {idx}: {numbers[idx]}")
            except ValueError:
                print("Помилка: індекс має бути цілим числом.")
            except IndexError:
                print("Помилка: індекс за межами списку!")

        elif choice == "5":
            try:
                idx = int(input("Введіть індекс елемента для видалення: "))
                deleted = numbers.pop(idx)
                print(f"Елемент {deleted} за індексом {idx} видалено.")
                print("Новий список:", numbers)
            except ValueError:
                print("Помилка: індекс має бути цілим числом.")
            except IndexError:
                print("Помилка: індекс за межами списку!")

        elif choice == "0":
            print("Вихід з програми.")
            break

        else:
            print("Невірний пункт меню. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
