total = 0

while True:
    user_input = input("Введіть додатнє число ( Enter або кінець для завершеня):")
    if user_input == "":
        break

    try:
        number = float(user_input)
        if number >= 1:
            total += number
        else:
            print("помилка . введене число від'ємне")
    except ValueError:
        print("помилка. ви ввели не число")

print(f"сума всіх чисел : {total} ")