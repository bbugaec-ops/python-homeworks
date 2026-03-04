def polina(n):
    s = str(abs(n))
    if s == s[::-1]:
        print("Це поліндром :",True)
    else:
        print("Не поліндром :",False)

n = int(input("введіть числа :"))

polina(n)
