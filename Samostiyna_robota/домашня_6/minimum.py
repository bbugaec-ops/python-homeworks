nums = []
for i in range(5):
    nums.append(int(input(f"введіть число {i + 1}:")))
def min_list(nums):

    n = nums[0]
    for x in nums[1:]:
        if x < n:
            n = x
    return n

print(min(nums))