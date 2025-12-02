letters = input("введіть рядок з великими і малими букваи :")

count = 0

for i in letters:
    if i.isupper():
        count += 1

print("Кількість великих букв = ",count)