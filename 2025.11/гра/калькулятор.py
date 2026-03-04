#   Вводимо меню для користувача

print("Калькулятор :")
print("Оберіть операцію : +, -, *, /")

# отримуємо операцію від користувача
operation = input("Введіть операцію:")

# запитати користувача перше і друге число

num1 = float(input("Введіть перше число:"))
num2 = float(input("Введіть друге число:"))

#  виконуємо відповідну операцію на основі введення користувача

if operation == '+':
    result = num1 + num2
    print(f"Результат: {num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"Результат: {num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"Результат: {num1} * {num2} = {result}")
elif operation == '/':
    if num2 / 0:
        print("Помилка: на нуль ділити неможна :")
    else:
        result = num1 / num2
        print(f"Результат: {num1} / {num2} = {result}")
else:
    #  якщо введено невірний символ операції
    print("Невірний вибір операції , спробуйте ще .")