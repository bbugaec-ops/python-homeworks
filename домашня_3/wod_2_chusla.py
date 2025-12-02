a = int(input("введіть перше число :"))
b = int(input("введіть друге число :"))

for i in range(a,b + 1):
    print(i)


print("числа в зворотньому напрямку :")
for i in range(b,a -1, -1):
    print(i)

