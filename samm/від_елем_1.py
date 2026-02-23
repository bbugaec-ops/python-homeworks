n = int(input("Введи кількість елементів списку :"))
a = [1] * n
print(a)
for i in range(n):
    a[i] = input(f"Введи {i} елемент списку :")
print(a)
