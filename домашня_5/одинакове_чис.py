nums = [1,2,3,5,2,1,3,0,3]
target = 3                       #  змінна яка зберігає просто число 3
count = 0                #    счотчик
for i in nums:
    if i == target:
        count += 1
print("Чило 3 зусрічається -",count,"рази ")