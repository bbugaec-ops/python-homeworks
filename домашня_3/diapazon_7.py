a = int(input("Введіть перше число :"))
b = int(input("Введіть друге число :"))

print("Ці числа діляться на 7 :")

for i in range(a, b + 1):
    if i % 7 == 0:
        print(i)
