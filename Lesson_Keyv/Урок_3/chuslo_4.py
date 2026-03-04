width = int(input("Введіть ширину прямокутника: "))
height = int(input("Введіть висоту прямокутника: "))

for i in range(height):
    for j in range(width):
        print('*', end='')
    print()
