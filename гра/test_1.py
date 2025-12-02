"""zakupy = {}
magazyn = {'яблука':15, 'apples':18, 'chery': 22, 'banana':8, 'lemon':14, 'orange':21}

try:
    print(magazyn['apples'])
    print(magazyn['lemon'])
    print(magazyn['kardamon'])
except KeyError:
    print("Ви ввели не існуючий продукт")

if 'kardamon' in magazyn:
    print(magazyn['kardamon'])
else:
    print('Ключа такого нема')

if 'lemon' in magazyn:
    print(magazyn['lemon'])
else:
    print('None')

print('-------------------------')

magazyn["chery"] = 16
print(magazyn) """

books = {
    "І.Котляревський": "Енеїда",
    "М.Гоголь": "Тарас бульба",
    "Т.Шевченко": "Гайдамаки",
    "О.Гончар": "Собор"
}
print(books)
k= len(books)
print(k)

"""del books["О.Гончар"]
print(books)

print(books.keys())
print(books.values())

print(list(books.keys()))
print(list(books.values()))    #     Перетвореня в список значень

print()
other = {"І.Франко": "Лис Микита"}
books.update(other)                       #   додоємо в Словник новий елемент новий Ключ і Значення
print(books)"""

print()

for key in books:
    print(key,"-",books[key])
print()

for val in books.values():
    print(val)

