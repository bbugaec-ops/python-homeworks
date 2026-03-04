def product_range(a, b):
    if a > b:
        a, b = b, a
    res = 1
    for i in range(a, b + 1):
        res *= i
    return res

print(product_range(1, 5))
