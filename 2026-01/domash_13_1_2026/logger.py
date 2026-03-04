"""  Завдання 3
Користувач вводить з клавіатури набір чисел та шлях до файлу для збереження отриманих даних. Вам необхідно:

зберегти усі отримані числа;
знайти максимум та мінімум. Ці значення збережіть у тому ж файлі;
вивести числа;
вивести максимум та мінімум;
створити клас для логування операцій. При створенні об'єкта класу зазначте, де виконується логування:
на екрані або у файлі. У програмі ви можете створити лише один об'єкт класу. Усі дії програми логуйте за допомогою об'єкта
цього класу."""

class Logger:
    def __init__(self, mode, file_path=None):
        self.mode = mode
        self.file_path = file_path

    def log(self, message):
        if self.mode == "console":
            print("[LOG]", message)
        elif self.mode == "file":
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write("[LOG] " + message + "\n")


# вибір логування
mode = input("Логування (console/file): ")

if mode == "file":
    log_path = input("Шлях до файлу логів: ")
    logger = Logger(mode, log_path)
else:
    logger = Logger("console")

logger.log("Програма запущена")

# введення чисел
numbers_input = input("Введіть числа через пробіл: ")
logger.log("Користувач ввів числа")

numbers = list(map(int, numbers_input.split()))

# шлях для збереження
data_path = input("Введіть шлях до файлу для збереження: ")
logger.log("Отримано шлях для збереження")

# обчислення
minimum = min(numbers)
maximum = max(numbers)

logger.log(f"Знайдено min={minimum}, max={maximum}")

# збереження у файл
with open(data_path, "w", encoding="utf-8") as f:
    f.write("Numbers:\n")
    f.write(" ".join(map(str, numbers)) + "\n")
    f.write(f"Min: {minimum}\n")
    f.write(f"Max: {maximum}\n")

logger.log("Дані записані у файл")

# вивід
print("Числа:", numbers)
print("Мінімум:", minimum)
print("Максимум:", maximum)

logger.log("Програма завершена")


