# функції вищого порядку
#from урок_8.main import userName

#studBirthYear = [2000,1997,2002,1999]
#print(studBirthYear)
#studAges = []

#for year in studBirthYear:
 #   studAges.append(2025 - year)
#studAges = list(map(lambda x: 2025 - x, studBirthYear))

#print(studAges)

#print('----------------')

#number = int(input(""))
#print(abs(number))

print('---------------')

def makeLog(userName,maker):
    return maker(userName)

def nameUper(name):
    return 'user' + name.upper()

def nameLower(name):
    return  'user' + name.lower()

print(makeLog("admin",nameUper))

print('-------------------')
#  map()   filter()     zip()

userLogs = ['admin','STUDENT','QWERty','User']
print(userLogs)

userLogsLow = list(map(str.lower,userLogs))
print(userLogsLow)

values = ['2.3','12','45.34','3']
print(values)
print('-------------------------')

numbers = list(map(float,values))
print(numbers)

print('----------------')

digits = list(map(lambda num: int(num[0]),values))
print(digits)

print('-----------------')

nums1 = [10,20,30]
nums2 = [1,2,3]
result = list(map(lambda a,b: a ** b, nums1, nums2))
print(result)

print('---------------------')

prices = [100,33,67,99,45]
expensive = list(filter(lambda x: x > 50,prices))
print("початкова ціна -",prices)
print("відфільтрована -",expensive)

print('------------------')

userPass = ['1111','qwer','3232']

for log,passw in zip(userLogs,userPass):
    print(f"login: {log}, password: {passw}")

print(list(zip(userLogs,userPass)))

print('--------------------')

numers = [-15,0,5,7,-20,25,30]
result = sorted(filter(lambda a: a > 0 and a % 5 == 0, numers))
print(result)
