userStr = "python1234"
digit = 0
letters = 0

for s in userStr:
    if s.isdigit():
        digit += 1
    elif s.isalpha():
        letters += 1
print(f"digits: {digit}")
print(f"letters:{letters}")