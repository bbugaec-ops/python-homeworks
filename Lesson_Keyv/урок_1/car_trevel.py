distance = float(input("Введіть скільки кілометрів :"))
paluvo = float(input("Введіть витрату палива :"))
prays = float(input("Введіть ціну палива :"))

trip_prays = (distance / 100) * paluvo * prays

print("Вартість поїздки буде коштувати :",trip_prays,"гр")