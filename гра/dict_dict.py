a = {
    1:'one',
    2:'two',
    3:'three',
    4:'трактор',
    5:'chery'
}
print(len(a))
print(3 in a, 7 in a, 9 not in a)

print('-------------------------')

if 6 in a:
    print(a[6])
else:
    a[6] = 'banana'
print(a)
print('----------------------------------------------------------------')


print(a.get(4))

print(a.setdefault(5))

print(a.setdefault(7,'seven'))
print(a)

print('--------------')

print(a.keys())

for key in a.keys():
   print(key, a[key])

print('--------------------------')

print(a.values())
print()
for value in a.values():
    print(value)

print('===============================')

print(a.items())
for para in a.items():
    print(para)
    print(para[0],para[1])