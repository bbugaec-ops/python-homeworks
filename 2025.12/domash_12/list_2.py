def spusok(nomer):
    s = 0
    try:
        for nom in range(9):
            s = s + nom
        return s
    except ValueError:
        print("Помилка")

my_spusok = (spusok(9))
print("Сума =",my_spusok)