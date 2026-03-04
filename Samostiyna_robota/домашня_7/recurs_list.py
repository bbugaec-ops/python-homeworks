def recu_sum(num_list):
    if not num_list:
        return 0
    else:
        return num_list[0] + recu_sum(num_list[1:])

my_numbers = list(range(1,101))

total = recu_sum(my_numbers)
print(f"Сума 100 чисел: {total}")