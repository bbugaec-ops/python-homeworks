from гра.array_sum import ProductArray, SumArray


class Product:
    def func1(self,arr):
        total = 1
        for x in arr:
            total *= x
        return total

    def func1(self,arr):
        total = 0
        for x in arr:
            total += x
        return total

    if __name__=="__main__":
        a =[3,5,2,4,6]
        print("Масив:",a)

        if a[0] > a[-1]:
            calc = ProductArray()
            print("Перше число більше останнього - Добуток(1-й клас)")
        else:
            calc = SumArray()
            print("Перше число не більше останнього - Сума(2-й клас)")

        result = calc.func1(a)
        print("Результ :",result)