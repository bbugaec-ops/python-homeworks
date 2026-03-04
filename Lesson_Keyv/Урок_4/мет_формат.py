str1 = 'hello python'
print(str1.center(50))
print(str1.center(50,"*"))

testSpace = "      space      "
print(testSpace.lstrip())
print(testSpace.rstrip())
print(testSpace.strip())

myStr1 = 'python !'
print(myStr1[0:6:2])
print(myStr1[0:8])
print(myStr1[:9:2])
print(myStr1[:9])
print(myStr1[:-1])

print(myStr1[:len(myStr1) // 2])

print(f"myStr1: {myStr1}, testSpace: {testSpace}")