snm = int(input("введіть перше число :"))
sum1 = int(input("введіть друге число :"))

print("Ці числа діляться на 5 :")

for i in range(snm, sum1 + 1):
    if i % 5 == 0:
        print(i)
print("А ці числа діляться на 7 :")
for i in range(snm,sum1 + 1):
    if i % 7 == 0:
        print(i)