sum = float(input("Ведіть перше число :"))
sum1 = float(input("Введіть друге число :"))
operation = input("Виберіть операцію + , - , / , * , **, % ,//:")



if operation == '+':
    print("сума буде = :",sum + sum1)
elif operation == '-':
    print("сума буде = ",sum - sum1)
elif operation == '*':
    print("сума буде = ",sum * sum1)
elif operation == '/':
     if sum1 != 0:
         print("сума буде = ",sum / sum1)
     else:
         print("на ноль ділити не можна")
elif operation == '//':
    print("сума буде = ",sum // sum1)
elif operation == '**':
    print("сума буде = ",sum ** sum1)
elif operation == '%':
    if operation != 0:

        print("сума залишок = ",sum % sum1)
    else:
        print("помилка")
else:
    print("не вірний вибір")
