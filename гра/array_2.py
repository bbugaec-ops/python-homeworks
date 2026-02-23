class SumArray:
    def func1(self,arr):
        total = 0
        for x in arr:
            total += x
        return total

class ProductArray:
    def func1(self,arr):
        total = 1
        for x in arr:
            total *= x
        return total


arr = [2,3,4,5]

s = SumArray()
p = ProductArray()

print("Масив:",arr)
print("Сума:",s.func1(arr))
print("Добуток:",p.func1(arr))