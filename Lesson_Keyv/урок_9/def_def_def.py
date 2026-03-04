# decoration


def simpleDecorator(func):
    print("Hello ! i am decorator !")

    def simpleWrapper():
        print("func start worcing !")
        func()
        print("end worcing !")

    return simpleWrapper()

def simpleDecorator_2(func):
    print("Hello ! i am decorator 2 !")

    def simpleWrapper():
        print("func start worcing !")
        func()
        print("end worcing !")

    return simpleWrapper()

def simpleDecorator_3(func):
    print("Hello ! i am decorator_3 !")

    def simpleWrapper(n1,n2):
        print("func start worcing !")
        result = func(n1,n2)
        func(n1,n2)
        print("end worcing !")

    return simpleWrapper()

def simpleDecorator_5(func):
    print("Hello ! i am decorator_5 !")

    def simpleWrapper(n1,n2):
        print("func start worcing !")
        result = func(n1,n2)
        print("end worcing !")
        return result

    return simpleWrapper()

@simpleDecorator
@simpleDecorator_2
def sayHi():
    print("Welcome !")

sayHi()

#sayHiPro = simpleDecorator(sayHi)

#sayHiPro
@simpleDecorator_3
@simpleDecorator_5
def addNums(num1, num2):
    return num1+num2

print(addNums(2,2))

def calcMultiplay(a,b):
    return a*b


def decoratorWrapper(argForDec):
    print(f"i have {argForDec}")




decotiongWithArg = decoratorWrapper(10)
calcMultiplayPro = decotiongWithArg(calcMultiplay)

print(calcMultiplay(3,3))


print('--------------------------')

