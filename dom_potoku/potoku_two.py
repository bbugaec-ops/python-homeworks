"""  Завдання 2
Користувач вводить з клавіатури шлях до файлу, що містить набір чисел. Після чого запускаються два потоки.

Перший потік створює новий файл, в який запише лише парні елементи списку. Другий потік створює новий файл,
в який запише лише непарні елементи списку.
Кількість парних і непарних елементів виводиться на екран.
 """
import threading

def read_numbers(path):

    with open(path, "r", encoding="utf-8") as f:
        test = f.read()
    return [int(x) for x in test.split()]


def write_evens(nums, out_path, result):
    evens = [n for n in nums if n % 2 == 0]
    with open(out_path, "w", encoding="utf-8") as f:
        for n in evens:
            f.write(str(n) + "\n")
    result["even"] = len(evens)

def write_odds(nums, out_path, result):
    odds = [n for n in nums if n % 2 != 0]
    with open(out_path, "w", encoding="utf-8") as f:
        for n in odds:
            f.write(str(n) + "\n")
    result["odd"] = len(odds)

def main():

    #in_path = "numbers.txt"

    in_path = input("Введіть шлях до файлу:").strip()


    nums = read_numbers(in_path)

    result = {"even": 0, "odd": 0}

    t1 = threading.Thread(target=write_evens, args=(nums, "even.txt", result))
    t2 = threading.Thread(target=write_odds, args=(nums, "odd.txt", result))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Парних:", result["even"])
    print("Непарних:", result["odd"])
    print("Готово: even.txt і odd.txt створені.")

if __name__ == "__main__":
    main()
