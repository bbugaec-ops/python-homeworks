# Програма "Фірма"
firm = {
    "Брюханов Олег Васильович": ["083456781", "oleg@company.com", "Нач-цех", 12, "oleg.skype"],
    "Дембіцький Віталій Мартинович": ["0234788665", "vitaliy@company.com", "Зам", 3, "vitaliy.skype"],
    "Пясківський Ігор Тарасович": ["046389423", "ihor@company.com", "Виховна-робота", 8, "ihor.skype"],
    "Костевська Людмила Романівна": ["035579482", "lyudmyla@company.com", "Директор", 1, "lyudmyla.skype"]
}


for pib, info in firm.items():
    print(f"\nПрацівник: {pib}")
    print(f"  Телефон: {info[0]}")
    print(f"  Email: {info[1]}")
    print(f"  Посада: {info[2]}")
    print(f"  Кабінет: {info[3]}")
    print(f"  Skype: {info[4]}")
