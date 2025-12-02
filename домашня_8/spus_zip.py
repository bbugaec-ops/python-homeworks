numbers = [1,2,3]
number1 = [4,5,6]

zipper = [a + b for a, b in zip(numbers,number1)]
print(zipper)

print('--------------------------')

chis = [1,2,3]
chis1 = [4,5,6]

zum = list(zip(chis,chis1))
print(zum)

print('-----------------------')

chusla = [1,2,3]
chusla1 = [4,5,6]

ziper = zip(chusla, chusla1)

flat = [x for pair in ziper
        for x in pair]
print(flat)
