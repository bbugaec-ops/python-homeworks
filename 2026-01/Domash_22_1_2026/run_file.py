import threading

def search_word_in_file(path: str, word: str, result: dict):
          #       шлях до файлу, слово яке шукає
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            #                                    криві символи ігноруємо
            found_lines = []

            for line_no, line in enumerate(f, start=1):
                if word in line:
                    found_lines.append(line_no)

        result["found"] = len(found_lines) > 0
        result["count"] = len(found_lines)
        result["lines"] = found_lines


    except FileNotFoundError:
        result["error"] = "Файл не знайдено"


    except Exception as e:
        result["error"] = f"Помилка: {e}"

def main():
    path = input("Введіть шлях до файлу: ").strip()
    word = input("Введіть слово для пошуку: ").strip()

    result = {}

    t = threading.Thread(target=search_word_in_file, args=(path, word, result))
    t.start()
    t.join()

    if "error" in result:
        print(result["error"])
        return

    if result["found"]:
        print(f" Слово '{word}' знайдено.")
        print(f"Кількість рядків : {result['count']}")
        print("Номер рядка :", result["lines"])
    else:
        print(f" Слово '{word}' НЕ знайдено.")

if __name__ == "__main__":
    main()
