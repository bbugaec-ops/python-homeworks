capitals = {"USA":"Washington",
            "India":"New Delli",
            "China":"Pekin",
            "France":"Paris"}

capitals.update({"Germany":"Berlin"})
print(capitals)


capitals.update({"USA":"Kiev"})
print(capitals)

capitals.pop(("China"))
print(capitals)




for el in capitals.keys():
    print(el)
print()

for ell in capitals.values():
    print(ell)

if capitals.get("Japan"):
    print("Є такаї країни")
else:
    print("Нема такої країни")

print()

values = capitals.values()    #   верне список
print(values)

print()

for key, value in capitals.items():
    print(f"{key}: {value}")
