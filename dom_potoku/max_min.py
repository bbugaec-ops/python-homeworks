"""  Завдання 1
Користувач вводить з клавіатури значення у список. Після чого запускаються два потоки.
Перший потік знаходить максимум у списку.
Другий потік знаходить мінімум у списку. Результати обчислень виведіть на екран.
 """


import threading

nums = list(map(int,input("Введіть числа через пробіл: ").split()))

result = {"max": None, "min": None}

def fin_max():
    result["max"] = max(nums)

def fin_min():
    result["min"] = min(nums)


t1 = threading.Thread(target=fin_max())
t2 = threading.Thread(target=fin_min())

t1.start()
t2.start()

t1.join()
t2.join()

print("Максимум:" , result["max"])
print("Мінімум:" , result["min"])