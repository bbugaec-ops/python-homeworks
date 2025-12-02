age = int(input("вкажіть ваш вік :"))
if age >=7 and age <=18:
    print("школяр")
elif age > 19 and age <= 25:
    print("молодик")
elif age > 25 and age <= 60:
    print("робітник")
elif age > 61:
    print("пенсіонер")
else:
    print("малюк або непонятний вік")