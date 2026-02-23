a = int(input("Введіть перше число: = "))
b = int(input("Введіть друге число: = "))

for i in range(a, b + 1):
    print("Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) or i)
