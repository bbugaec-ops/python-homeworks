class ProductArray:
    def func1(self,arr):
        total = 1
        for x in arr:
            total *= x
        return total

class SumArray:
    def func1(self,arr):
        total = 0
        for x in arr:
            total += x
        return total

if __name__=="__main__":
    a = []
    print("Введи 5 чисел:")

    for i in range(5):
        num = float(input(f"a[{i+1}] = "))
        a.append(num)

        print("\nМасив:",a)

        if a[0] > a[-1]:
            calc = ProductArray()
            print("Перше число > останнього - рахуємо добуток(1й клас)")
        else:
            calc = SumArray()
            print("Перше число < останнього - рахуємо суму (2й клас)")

        result = calc.func1(a)
        print("Результат :",result)