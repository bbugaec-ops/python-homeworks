with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

if lines:
    lines = lines[:-1]   # видаляємо останній рядок

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
