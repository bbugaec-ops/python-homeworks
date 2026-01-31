import random
import threading


numbers = []



filled_event = threading.Event()            # Сигнал для "список заповнено"

# Результати
sum_result = None
avg_result = None

def fill_list(n: int, a: int, b: int):
    """1-й потік: заповнює список випадковими числами."""

    global numbers
    local = [random.randint(a, b) for _ in range(n)]
    numbers = local                            # одним присвоєнням, щоб інші бачили готовий список
    filled_event.set()


def calc_sum():
    """2-й потік: чекає, потім рахує суму."""

    global sum_result
    filled_event.wait()  # чекати заповнення
    sum_result = sum(numbers)


def calc_avg():
    """3-й потік: чекає, потім рахує середнє."""

    global avg_result
    filled_event.wait()             # чекати заповнення
    avg_result = sum(numbers) / len(numbers) if numbers else 0

if __name__ == "__main__":
    n = 20          #         скільки чисел у списку
    a, b = 1, 100   #       діапазон випадкових чисел


    t1 = threading.Thread(target=fill_list, args=(n, a, b))
    t2 = threading.Thread(target=calc_sum)
    t3 = threading.Thread(target=calc_avg)


    t2.start()
    t3.start()
    t1.start()


    t1.join()
    t2.join()
    t3.join()

    print("Список:", numbers)
    print("Сума:", sum_result)
    print("Середнє:", avg_result)
