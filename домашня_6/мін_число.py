num = [3,7,9,1,-6,45]

def chis(nums):
    if not nums:
        return None
    m = nums[0]
    for x in nums[1:]:
        if x < m:
            m = x
    return m


print(chis(num))
