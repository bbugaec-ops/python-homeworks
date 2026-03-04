a = [['lviv',45],['kiyev',78],['junomur',24]]

f = dict(a)
print(f)       #   виведе словарь тільки якщо ключі будуть Слова не цифри

print('---------------------')

d = {
    'lviv':45,
    'kiyev':78,
    'jutomur':24
}
print(d)
del d['lviv']      #    идаляємо один обєкт
print(d)

print('----------------------')

w = dict(lviv=45,kiyev=78,jutomur=24)
print(w)

print('============================')

q = dict.fromkeys(['a','b','c'],45)
print(q)

print(len(d))
print(len(w))

z = {
    1:'one',
    2:'two',
    3:'three',
    4:'трактор'
}
print(4 in z,5 in z, 7 not in z)