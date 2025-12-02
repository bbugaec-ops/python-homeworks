nums = [1,2,3]
print(nums[0])

student_info = ["Bob",19,11]
print(f"Name: {student_info[0]}")

print()

st_info_dict = {"name":"Bob",    #   СЛОВНИК
                "age":19,
                "avg":11}
print(st_info_dict)
print(type(st_info_dict))

bookDict = {
          'auther':'Gvido van Rossun',
          'title' :'Python course',
          'price' : 230,
          'pages' : 550
}
print(bookDict)
print()

myDict1 = dict([("a",111),("b",222),("c",333)])
print(myDict1)

keyList = ['a','b','c']
valueList = [111,222,338]
myDict2 = dict(zip(keyList,valueList))
print(myDict2)

myDict3 = dict(firstName = "Bill",lastName = "Geits")
print(myDict3)

emptyDict = {}
emptyDict['newKey'] = 111
emptyDict['newKey'] = 22222         #   привязуємо інше значення
print(emptyDict)

print(len(bookDict))    #   це показує довжину

print()

#newKey = input("Enter new prop of book -")
#bookDict[newKey] = input("Enter new value -")
#print(bookDict['language'])

print()

for key in bookDict:
    print(f"{key}: {bookDict[key]}")