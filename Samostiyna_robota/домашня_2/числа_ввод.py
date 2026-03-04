chyslo_1 = float(input("введіть перше число :"))
chyslo_2 = float(input("введіть друге число :"))
chyslo_3 = float(input("введіть третє число :"))

choice = input("Введіть '+' щоб обчислити сумму або '*' щоб обчислити добуток :")

if choice == '+':
    print("Сума трьох чисел = ", chyslo_1 + chyslo_2 + chyslo_3)
elif choice == '*':
    print("Добуток трьох чисел = ", chyslo_1 * chyslo_2 * chyslo_3)
else:
    print("Невірний вибір дій")