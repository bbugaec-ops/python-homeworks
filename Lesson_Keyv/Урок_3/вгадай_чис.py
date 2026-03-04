import random

print("Я загадав число від 1 до 100. Спробуй відгадати!")

secret = random.randint(1, 100)
guess = 0
attempts = 0

while guess != secret:
    guess = int(input("Введи число: "))
    attempts = attempts + 1

    if guess < secret:
        print("Моє число більше.")
    elif guess > secret:
        print("Моє число менше.")
    else:
        print("Ти вгадав число за", attempts, "спроб !")
