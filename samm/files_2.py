# 1. Записуємо текст у файл
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("Привіт, це текст у файлі!")

print()

with open("text.txt",'r',encoding='utf-8') as f:
    content = f.read()
    print("Довжина файлу :",len(content))

print()

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()
    print("Довжина:", len(text))
