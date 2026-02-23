#  винятки
from урок_8.main import discount

print("Hello")
#print(2 + "4")
#print(2/0)       помилки

#try except

#    try:   перевіряє чи є помилка
#  except:  ловить помилку
#
#
# try:
#      amount = int(input("Enter the amount of received items -"))
#      items_type = input("Enter the type of items - ")
#      parts_number = int(input("Enter the number of perts"))
#      part_amount = amount / parts_number
#      print(f"Supply of {amount},{items_type} saved !")
#
#
# except (ValueError,TimeoutError):
#      print("Amount should be an integer !")
# except ZeroDivisionError:
#     print("Cant division by zero !")
# except Exception as ex:
#     print("We have some error", ex)
# finally:
#     print("Programa has finished")
#
#


#try:
#      amount = int(input("Enter the amount of received items -"))
#      items_type = input("Enter the type of items - ")
#      parts_number = int(input("Enter the number of perts"))
#      part_amount = amount / parts_number
#      print(f"Supply of {amount},{items_type} saved !")
# except:
#      print("Amount shold be an integer !")
#
# try:
#     num = int(input("Enter num -"))
#     print(num ** 2)
# except ValueError:
#     print("Error ! Need a number !")
# else:  #   working error
#     print("All is good ")
# finally:   # always working
#     print("Programa has finished !")
#
# #
#
# try:
#     salary = int(input("Enter salary -"))
#     if salary < 0:
#         raise Exception('Salary must be positive')
# except Exception as ex:
#     print("Error :",type(ex).__name__,ex)
#
#
# print('Final price calculating')
# try:
#     price = float(input("Enter start price"))
#     discount = float(input("Enter percent of discount"))
#     if discount < 0 or discount > 100:
#         raise  ValueError("Parcent must be > 0 and , 100 !")
#     final_price = price * (1 - discount / 100)
#     print(f"Final price of product: {final_price:.2f} uah")
# except ValueError as ex:
#     print(f"Input error :{ex}")
# finally:
#     print("Calculator finished !")

print()

try:
    dollar = float(input("введіть суму в доларах"))
    wert = float(input("введіть курс долара до євро"))

    if wert == 0:
        raise Exception("курс може дорівнювати нулю")
    euro = dollar * wert
    print(f"сума в євро",{euro})


except ValueError:
    print("помилка введено неправельно")

except ZeroDivisionError:
    print("не може дорівнювати нулю")

finally:
    print("операцію завершено")

print()

try:
    students = input("Введіть оцінки студентів -")
    input = students.split()

    ask = []

    for p in input:
        ask.append(float(p))

    if len(ask) == 0:
        raise ZeroDivisionError("Порожньо")

    total = 0

    for g in ask:
        total += g

    averange = total / len(ask)
    print("Середня оцінка",averange)

except ValueError:
    print("Помилка не ті дані")

except ZeroDivisionError:
    print("список порожній")
finally:
    print("завершення")






