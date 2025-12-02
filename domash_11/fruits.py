foods = []
prices = []
total = 0

while True:
    food = input("Enter food duy (q to qyit :")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("\nYour list :")
for food,price in zip(foods,prices):
    print(f"{food} - $ {prices}")