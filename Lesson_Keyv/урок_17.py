numbers = [1,2,3,4,5,6,7,8,9]

plus_ten = list(map(lambda x: x + 10,numbers))
print("Numbers + 10:",plus_ten)

print('-------------------')

number = [1,2,3,4,5,6,7,8,9]

even = list(filter(lambda x: x % 2 == 0,number))
print("Even number:",even)

print('-------------------')

number1 = [1,2,3,4,5,6,7,8,9]

squared = list(map(lambda x: x * x, number1))
print("Squared number1:", squared)

print('-------------------')

number2 = [1,2,3,4,5,6,7,8,9]

plus_ten = list(map(lambda x: x + 10, number2))
even = list(map(lambda x: x % 2 == 0, number2))
squared = list(map(lambda x: x * x,number2))

print("Number2 + 10:",plus_ten)
print("Even number2:",even)
print("Squared number2:",squared)