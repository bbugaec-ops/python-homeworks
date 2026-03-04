
print("парні числа в діапазоні:")


def para(a,b):

    for i in range(a, b + 1):
     if i % 2 == 0:
         print(i)
para(2,11)