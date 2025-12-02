try:
    find_word = input("Введіть слово, яке потрібно знайти: ").strip()
    replace_word = input("Введіть слово, на яке замінити: ").strip()

    with open("slovo.txt", "r", encoding="utf-8") as f:
        text = f.read()

    new_text = text.replace(find_word, replace_word)

    with open("slovo.txt", "w", encoding="utf-8") as f:
        f.write(new_text)

    print("Готово! Слово замінено.")

except FileNotFoundError:
    print("Файл slovo.txt не знайдено!")

except Exception as e:
    print("Сталася помилка:", e)
