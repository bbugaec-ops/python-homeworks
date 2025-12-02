text = input("введіть рядок з символами '@#$%&':")

for ch in '@#$%&':
    text = text.replace(ch, "")
print(text)