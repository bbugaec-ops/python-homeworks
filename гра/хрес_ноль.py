# Створюємо поле 3х3
pole = [["[_]", "[_]", "[_]"],
        ["[_]", "[_]", "[_]"],
        ["[_]", "[_]", "[_]"]]

# Функція для виводу поля
def print_pole():
    for row in pole:
        print(" ".join(row))
    print()

# Перевірка на перемогу
def check_win(symbol):
    # перевірка рядків і стовпців
    for i in range(3):
        if all(pole[i][j] == symbol for j in range(3)):  # рядок
            return True
        if all(pole[j][i] == symbol for j in range(3)):  # стовпець
            return True
    # діагоналі
    if all(pole[i][i] == symbol for i in range(3)):
        return True
    if all(pole[i][2-i] == symbol for i in range(3)):
        return True
    return False

print("Починаємо гру Хрестики-Нулики!")
print_pole()

# Гра максимум 9 ходів
for move in range(9):
    if move % 2 == 0:
        symbol = "[X]"
        print("Хід гравця X")
    else:
        symbol = "[O]"
        print("Хід гравця O")

    row = int(input("Введіть номер рядка (1-3): ")) - 1
    col = int(input("Введіть номер стовпця (1-3): ")) - 1

    # якщо клітинка вільна
    if pole[row][col] == "[_]":
        pole[row][col] = symbol
    else:
        print("Клітинка зайнята! Пропуск ходу.")
        continue

    print_pole()

    # перевіряємо на перемогу
    if check_win(symbol):
        print("Переміг гравець", symbol)
        break
else:
    print("Нічия!")
