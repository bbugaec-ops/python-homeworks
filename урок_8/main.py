# лямбда вираз- lambda -анонімна функція і яка немає назви
# lambda -аргументи1,2,3: вираз-дія

def add10(x):
    return x +10

nums = [1,2,3,4,5]
#for num in nums:
 #   print(add10(num))

for num in nums:
    print((lambda x: x+10)(num))
print('-----------------')

students = [['Bob',70],
            ['Jane',80],
            ['Piter',60]]

print(students)
sortedSts = sorted(students,key=lambda x:x[1])
print(sortedSts)

print('----------------')

grnToDollar = 42
discount = 0.15
priceDol = lambda x: x / grnToDollar * (1 - discount)

price = 4200
print(f"Price : {priceDol(price)} $")
print(f"Price : {priceDol(3500)} $")

print('--------------')

userName = lambda firstName, lastName:f"Full name: {firstName.title()} {lastName.title()} "

print(userName("mell","gibson"))

print('----------------')


wer = lambda x: x ** 2

num = int(input("введіть число :"))
print("квадрат числа",wer(num))

print('--------------')

big = lambda a,b: a if a > b else b

x = 12
y = 7
print(big(x,y))

print('---------------')

even = lambda x: x % 2 == 0

print(even(4))
print(even(7))

print('--------------')

#  лямбда це - спосіб створення анонімної функції яка містить одне вираженя.
#    використовується для написання коротких і простих функцій

print('-------------------')

#  функції вищих порядків





