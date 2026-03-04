meters = float(input("Введіть кількість метрів: "))
meters_1 = input("Введіть Yes або No: ")

centimeters = meters * 100
decimeters = meters * 10
miles = meters / 1609.34

print("Метрів у сантиметрах:", centimeters)
print("Метрів у дециметрах:", decimeters)
print("Метрів у милях:", miles)

if meters_1.lower() == 'yes':
    print("Всі міри довжини:",'сантіметри = ',centimeters,', дециметри = ',decimeters,', милі = ',miles)
else:
    print("Немає такої міри довжини.")
