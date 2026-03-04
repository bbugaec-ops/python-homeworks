
def is_prime(n):
    if n < 2:
        return  False
    for d in range(2,int(n**0.5)+1):
        if n % d == 0:
            return False
        return True

print(is_prime(2))
print(is_prime(9))
print(is_prime(13))