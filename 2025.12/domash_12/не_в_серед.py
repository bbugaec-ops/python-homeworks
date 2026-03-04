def divide(a,b):
    return a / b

def main():
    try:
        x = float(input("введіть перше число :"))
        y = float(input("введіть друге число :"))
        result = divide(x,y)
        print("Результат :",result)
    except ValueError:
        print("Помилка . треба вводити числа")
    except ZeroDivisionError:
        print("Помилка .ділити на нуль не можна")

main()