def divide_saf(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка . на нуль ділити не можна :")
        return None
def main():
    try:
        x = float(input("Введіть перше число :"))
        y = float(input("Введіть друге число :"))
    except ValueError:
        print("Помилка. треба вводити числа :")
        return

    result = divide_saf(x,y)
    if result is not None:
        print("Результат :",result)

main()
