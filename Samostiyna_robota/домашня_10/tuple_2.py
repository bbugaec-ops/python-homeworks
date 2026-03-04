a = (1,2,3,4)
b = (9,2,7,4)
c = (0,2,8,4)

result = []

for x,y,z in zip(a,b,c):
    if x == y == z:
        result.append(x)
        
print(result)