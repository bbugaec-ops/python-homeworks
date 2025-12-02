person = {'first_name': 'Альбіна', 'last_name': 'Шовкопляс'}
print(person.keys())
print(person.values())

# dict_keys(['first_name', 'last_name'])
# dict_values(['Альбіна', 'Шовкопляс'])

#  Ітераця по еллементам словника
person = {'first_name': 'Валерій', 'last_name': 'Макаренко','Name_name':"Vasuly"}

for key, value in person.items():
    print(f'{key}: {value}')

# first_name: Валерій
# last_name: Макаренко

#  Оновлення словника елементами з іншого словника
fruits = {'apple': 'яблуко', 'orange': 'апельсин','shokolade':'millk'}
fruits.update({'kiwi': 'ківі', 'pear': 'груша','Chery':'вишня'})

print(fruits)

# {'apple': 'яблуко', 'orange': 'апельсин', 'kiwi': 'ківі', 'pear': 'груша'}

