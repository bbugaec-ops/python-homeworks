prices = {"яблука":15,"банани":20,"вишні":16,"помідори":32,"огірки":24}

product = input("Введіть назву товару :").lower()


if product in prices:
    print(f"Ціна товару '{product}': {prices[product]}")
else:
    print("Такого товару нема .")