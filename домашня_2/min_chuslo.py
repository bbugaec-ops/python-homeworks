
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))


choice = input("Ваш вибір (1/2): ")

if choice == "1":
    print("Максимум із трьох чисел:", max(a, b, c))
elif choice == "2":
    average = (a + b + c) / 3                         #    Формула середнього арифметичного числа
    print("Середнє арифметичне трьох чисел:", average)
else:
    print("Невірний вибір :")
