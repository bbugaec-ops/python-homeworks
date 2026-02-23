import random

n = 20
secret = [random.randint(-10,10) for i in range(n)]
print("Список :",secret)

positives = [x for x in secret if x > 0]
negatives = [x for x in secret if x < 0]    # Чесно половину я написав ,а половину чат

min_positive = min(positives) if positives else None
max_negetive = max(negatives) if negatives else None

pozi = sum(1 for x in secret if x > 0)
nega = sum(1 for x in secret if x < 0)
zero = secret.count(0)

print("Мінімальне додатнє :",min_positive )
print("Максимальне від'ємне :",max_negetive)
print("додотні числа :",pozi)
print("від'ємні числа :",nega)
print("кількість нулів :",zero)