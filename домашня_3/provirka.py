a = int(input("введіть перше число :"))
b = int(input("введіть друге число :"))



for i in range(a,b + 1):
    if i % 3 == 0:
        print("Fizz",i)
print()

for i in range(a,b + 1):
    if i % 5 == 0:
        print("Buzz",i)
print()

for i in range(a,b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz - Buzz",i)