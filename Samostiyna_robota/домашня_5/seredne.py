nums = []
for i in range(7):
    x = float(input(f"введіть число {i + 1}:"))
    nums.append(x)

avg = sum(nums) / len(nums)
print(f"Середнє: {avg: .2f}")
