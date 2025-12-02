# example 1
pricesUSD = [100,35,77,86,34]
print(pricesUSD)

def priceToGrn(priceList):
    return list(map(lambda x: x * 42,priceList))


def changePriceDecorator_1(func):
    print("Hello,")

    def simpleWrapper(argList):
        print("i have got pricec")             #    нарахування знижки
        result = func(argList)
        resultWithDesc = list(map(lambda x: x * (1-0.15),result))
        print("set a discount !")
        return resultWithDesc

    return simpleWrapper



priceGrineWithDesc  = changePriceDecorator_1(priceToGrn)
print(priceGrineWithDesc(pricesUSD))



print(priceToGrn(pricesUSD))

print('--------------------------')


import time


def checkTime(func):

    def wrapper(*args):
        startTime = time.time()
        result = func(*args)
        print(f"working time {time.time() - startTime}")
        return result

    return wrapper

@checkTime
def testFunc():
    print(f"func working")
    time.sleep(1)

testFunc()

print('-------------------------')


def prefix(func):
    def wrapper(*args):
        return ">> " + str(func(*args))
    return wrapper

@prefix
def hello():
    return "world"

print(hello())




