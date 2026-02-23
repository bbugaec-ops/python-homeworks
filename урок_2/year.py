year = int(input("Введіть рік :"))

if year % 4 == 0 and year % 100 != 0:
    print("Year is leap")
elif year % 400 == 0:
    print("Year is leap")
else:
    print("Year is not leap")