def student(name, age):
    if age < 18:
        return f"{name}: ви ще молодий-да"
    else:
        return f"{name}: ви можете вчитися"

print(student("Vasuly",19))
print(student("lida",17))

print('-------------------------------------')

def student1(name, age):
    if not isinstance(name,str) or name.strip() == "":
        return "Помилка . некоретне імя"

    if not isinstance(age,int):
        return "Помилка .Вік повинен бути числом"
    if age < 0 or age > 130:
        return "помилка неправельний вік"
    if age < 18:
        return f"{name}: ви ще молодий"
    else:
        return f"{name}: ви можете вчитися"

print(student1("Oleg",21))
print(student1("Igor",16))