
def square(a,b):
    return a+b

def cube(a,b):
    return a-b

def nugate(a,b):
    if b == 0:
        raise "Erorr"
    return a/b
def pozit(a,b):
    return a*b


def golov(c):
    if c == '1':
        return square
    elif c == '2':
        return cube
    elif c == '3':
        return nugate
    elif c =='4':
        return pozit
    else:
        return None
mnoz = input("виберіть операцію 1(+),2(-),3(/),4(*) :").strip()

myChot = golov(mnoz)
print(myChot(2,8))