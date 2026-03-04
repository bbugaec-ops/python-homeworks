# функції
def printMsg():
    print("hello funkcion")

printMsg()
printMsg()

print("hello","test")

def printMsgnew(msg):
    print(msg)

printMsgnew("new func")



def plusNams(num1,num2,num3):
    #print(num1+num2+num3)
    return num1+num2+num3

sum = plusNams(2,2,3)+20
print(sum)

if "2".isdigit():
    print("ok")

def checkLog(userLog):
    if userLog == 'admin':
        return userLog.lower()
    elif userLog == 'user':
        return userLog.upper()
    else:
        return "wrong str"


print(checkLog('admin'))
print(checkLog('user'))


def userGreetings(login,passw = "admin"):
    if login == 'admin':
        print("Welcome !")
    elif login == 'student':
        print("welcome stident !")
    else:
        print('welcome gay ')

userGreetings('student')
userGreetings('qwer')


# *args - праметри передає цілі списки в функцію
def sumOfNums(*args):
    print(list(args))
    sum = 0
    for elen in args:
        sum += elen
    return sum

nums = [1,3,5]

print(sumOfNums(1,3,5))




