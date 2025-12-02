file_name = input("Введіть назву файлу :")
word = input("Яке слово шукати :")

count = 0

with open('slovo.txt','r',encoding='utf-8') as f:
    for line in f:
        words = line.lower().split()
        count += words.count(word)
print(f"Слово {word} : зустрічається {count} раз")
