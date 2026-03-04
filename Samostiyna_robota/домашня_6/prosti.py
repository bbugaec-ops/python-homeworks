def is_prime(n):
    if n < 2:               #    0 i 1 - не прості числа
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def count_primes(nums):
    cnt = 0
    for x in nums:
        if is_prime(x):
            cnt += 1
    return cnt


print(count_primes([1, 3, 4, 5, 15, 17, 19, 20]))
