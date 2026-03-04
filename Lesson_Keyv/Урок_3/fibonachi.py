name_list = int(input("Введіть число :"))
total = 0
count = 0
for i in range(name_list + 1):
    count += 1    #              счотчик
    total += i    #                 число з якого все починається
    print("Total =", total)
print("Avg =",total/count)

