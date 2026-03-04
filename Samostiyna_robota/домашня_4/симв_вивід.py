text = input("Введіть якицсь текст :")

letters = digits = speces = others = 0

for h in text:
    if h.isalpha():          #  взнає скільки букв  і считає їх
        letters += 1
    elif h.isdigit():       #  цифер
        digits += 1
    elif h.isspace():          #   пробілів
        speces += 1
    else:
        others += 1        #     символи

print("Букви -",letters)
print("Цифри -",digits)
print("Пробіли -",speces)
print("Символи -",others)


