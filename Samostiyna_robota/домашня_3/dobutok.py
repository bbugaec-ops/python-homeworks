a = int(input("перше чило :"))
b = int(input("друге число :"))

sum4 = 0
for i in range(a ,b + 1):
    if i % 4 == 0:
       print(i)
       sum4 += i
print("Сума чисел на 4 =",sum4)

print("-----------------")

sum6 = 0
for i in range(a, b + 1):
    if i % 6 != 0:
       print(i)
       sum6 += i
print("Сума чисел не ділиться на 6 =",sum6)
print("------------")
if a > b:
    print("Сталася помилка , перше число неможе бути більшим за друге .")
