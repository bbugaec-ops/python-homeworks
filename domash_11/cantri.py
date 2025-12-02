cantri = {"France": "Paris","Japan":"Tokyo","UK":"London","Ukraine":"Kiyv","Italy":"Roma"}

for key, values in cantri.items():
    print(values,sep="")

print('--------------')

cantri1 = {"France":"Paris","Japan":"Tokio","UK":"London","Moldova":"Chichineu","Bolgaria":"Sofia"}

for el in cantri1.values():
    print(el)

print('--------------')

cantri2 = {"Franse":"Paris","Japan":"Tokyo","UK":"London","Moldova":"Chichineu"}

for el in cantri2.keys():
    print(el)