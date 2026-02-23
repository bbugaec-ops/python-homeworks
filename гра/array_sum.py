import random
from functools import reduce

class SumArray:
    def func1(self,arr):
        return sum(arr)

class ProductArray:
    def func1(self,arr):
        return reduce(lambda a,b: a * b, arr,1)


if __name__== "__main__":
    arr = [random.randint(7,14) for _ in range(4)]
    print("Масив:", arr)

#  індекси
    if arr[1] > arr[2]:
        calc = SumArray()
        print("2-ге число > 3-го рахуємо суму")
    else:
        calc = ProductArray()
        print("2-ге число < 3-го рахуємо добуток")

    result = calc.func1(arr)
    print("Результат:",result)

