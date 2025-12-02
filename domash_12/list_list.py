
def list_sum(number):
    try:
        total = sum(number)
        return total
    except TypeError:
        print("Помилка в списку")
        return None
    except Exception as e:
        print(f"Невідома помилка : {e}")

my_list = [1,2,3,4,5,6]
total = list_sum(my_list)
print(total)

print('--------------------------------------')

def list_list(nums):
    total = 0
    try:
        for number in nums:
            total += number
        return total
    except TypeError:
        print("Помилка це не список")
        return None

my_list1 = [2,4,5,'g',9]
print(list_list(my_list1))

print('--------------------------------------')

def spusok(nomer):
    s = 0
    try:
        for nom in range(9):
            s = s + nom
        return s
    except ValueError:
        print("Помилка")

my_spusok = (spusok(9))
print("Сума =",my_spusok)