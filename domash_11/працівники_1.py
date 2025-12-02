# Програма "Фірма"
# Збереження даних про працівників у словнику

firm = {
    "Брюханов Олег Васильович": {
        "phone": "083456781",
        "email": "oleg@company.com",
        "posada": "Нач-цех",
        "kabinet": 12,
        "skype": "oleg.skype"
    },
    "Дембіцький Віталій Мартинович": {
        "phone": "0234788665",
        "email": "vitaliy@company.com",
        "posada": "Зам",
        "kabinet": 3,
        "skype": "vitaliy.skype"
    },
    "Пясківський Ігор Тарасович": {
        "phone": "046389423",
        "email": "ihor@company.com",
        "posada": "Виховна-робота",
        "kabinet": 8,
        "skype": "ihor.skype"
    },
    "Костевська Людмила Романівна": {
        "phone": "035579482",
        "email": "lyudmyla@company.com",
        "posada": "Директор",
        "kabinet": 1,
        "skype": "lyudmyla.skype"
    }
}


for pib, data in firm.items():
    print(f"\n{pib}:")
    for key, value in data.items():
        print(f"  {key}: {value}")

while True:
    print("1 - Додати працівника")
    print("2 - Знайти працівника")
    print("3 - Видалити працівника")
    print("4 - Вийти")

    cmd = input("вибір :")

    if cmd == "1":
        pib = input("ПІБ:")

        phone = input("телефон:")
        email = input("емаіл:")
        posada = input("посада:")
        kabinet = input("кабінет:")
        skype = input("скайп:")

        firm[pib] = {"phone": phone,
                     "email": email,
                     "posada": posada,
                     "kabinet": kabinet,
                     "skype": skype }

        print("Працівника додано")

    elif cmd == "2":
        pib = input("Введіть ПІБ для пошуку:")
        res = firm.get(pib)

        if res:
            print(f"\n{pib}:")
            for key,val in res.items():
                print(f" {key}: {val}")
        else:
            print("Нема такого працівника")

    elif cmd == "3":
        pib = input("кого видалити (ПІБ) ?")

        if pib in firm:
            firm.pop(pib)
            print("працівника видалено")
        else:
            print("такого нема")
    elif cmd == "4":
        break
    else:
        print("невірна команда")