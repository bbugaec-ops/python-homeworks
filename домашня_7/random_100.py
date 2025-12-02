import random

random_num = [random.randint(-100,100) for  _ in range(100)]

def find_recursiv(number,index = 0, min_sum = float('inf'),min_index = 0):

    if index > len(number) - 10:
        return min_sum, min_index

    current_sum = sum(number[index : index + 10])

    if current_sum < min_sum:
        min_sum = current_sum
        min_index = index

    return find_recursiv(number,index + 1, min_sum, min_index)

min_sum_recurs,min_index_recurs = find_recursiv(random_num)
print(f"Мінімальна сума : {min_sum_recurs}")
print(f"Початок : {min_index_recurs}")


