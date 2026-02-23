text = input("введіть речення :")


if text == text[::-1]:      #     текст повертає назад
    print("поліндром :")
else:
    print("не поліндром :")

print()

if text == text[-1::]:
    print("не полін назад")
else:
    print("полін назад")

print()


for i in text:
    if text == text[::-1]:
        print("поліндром")
    else:
        print("не поліндром")