a = int(input("введіть перше число :"))
b = int(input("введіть друге число :"))

print("вперед напрямок :")
for i in range(a,b ,5):
    print(i)
print("---------------")

print("зворотній напрямок :")
for i in range(b,a - 1,- 5):
    print(i)
