def recurs_diln(a,b):
    if b == 0:
        return a
    else:
        return recurs_diln(b, a % b)

print("Найбільший дільник ",recurs_diln(48,18))
print('-----------------------')

def ddss(a,b):
    if b == 0:
        return a
    else:
        return ddss(b,a % b)     #   Формула Евкліда

num1 = 56
num2 = 98
result1 = ddss(num1,num2)
print(f"Найбільший дільник чисел {num1} та {num2}: {result1}")


num3 = 100    #  Якщо друге число = 0 , то перше число і є найбільшим дільником
num4 = 0
result2 = ddss(num3,num4)
print(f"Найбільший дільник {num3} i {num4}: {result2}")

num5 = 78
num6 = 18
result3 = ddss(num5,num6)
print(f"Найбільший дільник {num5} i {num6}: {result3}")