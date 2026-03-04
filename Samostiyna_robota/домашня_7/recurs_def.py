def sum_recurs(a,b):
    if a > b:
        return 0   #  якщо а більше за б  , то рекурсія припиняється

    else:
        return a + sum_recurs(a + 1, b)    # у виклик додаємо 'a' і викликаєм функцію для другого числа

start = 1
end   = 5
result = sum_recurs(start,end)
print(f"Сума чисел {start} до {end}: {result}")

"""    5 + 0 = 5  |  4 + 5 = 9  |   3 + 9 = 12  |  2 + 12 = 14   |   1 + 14 = 15   """
print('--------------------')

def sam_recurs(a,b):
    if a == b:
        return b
    else:
        return a + sam_recurs(a + 1, b)

start2 = 1
end2   = 8
result = sam_recurs(start2,end2)
print(f"Сума чисел {start2} до {end2} = {result}")

print("---------------------------------")

def som_recurs(a,b):
    if a > b:                     #  Тут припиняє роботу бо а більше за б
        return False

    else:
        return a + som_recurs(a + 1, b)

start3 = 5
end3   = 1
result = som_recurs(start3,end3)
print(f"Сума чмсел {start3} до {end3} = {result}")