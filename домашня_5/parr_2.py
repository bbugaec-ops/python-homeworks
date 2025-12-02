n = int(input())
nums = [int(input()) for _ in range(n)]   # сформували список
for x in nums:
    if x % 2 == 0:
        print(x)
