def remove_all(nums, target):
    b = nums.count(target)
    nums[:] = [a for a in nums if a != target]
    return b

data = [1,2,3,2,2,4,5,9,5,0,9]

print(remove_all(data, 5))
print(data)
