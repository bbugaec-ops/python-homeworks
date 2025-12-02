nums = list(map(float, input("Введіть 7 чисел через пробіл: ").split()))
if len(nums) != 7:
    print("Треба рівно 7 чисел.")
else:
    print(sum(nums) / len(nums))
