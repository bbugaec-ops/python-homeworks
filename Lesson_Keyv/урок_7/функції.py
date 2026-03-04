#  функції
def sayHello():
    name = "qwerty"
    print(f"Hello, {name}")

print(type(sayHello))

greeting = sayHello
greeting()
print()

customers = ['AdminJane','AdminBob','STUDENTNick','studentALICE','kate']
def sayHelloForClient(costomer):
    if costomer.find('admin') != -1:
        print(f'Hello admin - {costomer}')
    elif costomer.find('student') != -1:
        print(f'Hello student - {costomer}')
    else:
        print(f'Hello -{costomer}')

def greeting(costomerList,greenFunc):
    if isinstance(costomerList,list):
       for c in costomerList:
           greenFunc(c.upper())

greeting(customers,sayHelloForClient)
print()

def calculateSum(a,b):
    return a + b
def calculateMinus(a,b):
    return a - b
def calculateDel(a,b):
    if b != 0:
        return a / b
def userChoice(c):
    if c == '1':
        return calculateSum
    elif c == '2':
        return calculateMinus
    elif c == '3':
        return calculateDel

myCalculation = userChoice('3')
print(myCalculation(10,2))

print()

#  рекурсія це функція яка вивликає саме себе

def factorialCalculation(num):
    if num == 0:
        return 1
    else:
        print(num)
        return num * factorialCalculation(num - 1) # 5*factorialCa *4*3*2*1-(0)
print('---------------')
print(factorialCalculation(5))

print('--------------')


def isStrPalindrom(myStr):
    if len(myStr) == 0:
        return True
    else:
        if myStr[0] == myStr[-1]:
            print(myStr[1:-1])
            return isStrPalindrom(myStr[1:-1])
        else:
            return False
str1 = 'madam'
str2 = 'dana'
print(isStrPalindrom(str1))
print(isStrPalindrom(str2))
print('------------------------')

def fandMin(numberList):
    if len(numberList) > 1:
        return min(fandMin(numberList[:-1]),numberList[-1])
    else:
        return numberList[0]

nums = [2,4,1,8,10]
print("min = ",fandMin(nums))
print('----------------------')






