numbers = [2,5,7,23,34,53,67,87,95,123,456]
big_chus = list(filter(lambda x: x > 70,numbers))
min_chus = list(filter(lambda a: a < 70,numbers))


print(numbers)
print(big_chus)
print(min_chus)