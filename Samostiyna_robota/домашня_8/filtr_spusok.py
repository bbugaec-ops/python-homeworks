numbers = [1,2,3,],[3,4,5,]
asd = numbers[0] + numbers[1]
even = list(map(int, asd))
result = list(filter(lambda x: x % 3 == 0,even))
print(result)

