number = 100

# local and dlobal
def multiplyNums(num1,num2):
    global number   #  глобальне перезаписування
    number = 200
    print(number)
    # start local nemespace
    return num1 * num2

multiplyNums(2,2)
print(number)
