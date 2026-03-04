def show(a, b):
    for n in range(min(a, b) + 1, max(a, b)):
        if n % 2:
            print(n)

show(2,10)

print()



def maks(a,b):
    for i in range(max(a,b)):
        if i % 2 != 0:
            print(i)

maks(5,9)


def max4(a,b,c,d):
   return max(a,b,c,d)

a,b,c,d = map(float,input('ввести 4 числа').split())
print(max4(a,b,c,d))

