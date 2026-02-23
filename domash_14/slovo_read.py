with open("slovo.txt", "r", encoding="utf-8") as f:
    words = f.read().split()

for i, w in enumerate(words, start=1):
    print(f"{i}: {w}")
