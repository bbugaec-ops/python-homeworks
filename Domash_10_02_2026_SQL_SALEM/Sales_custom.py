import sqlite3


def run_sales_db():
    # 1. Створення бази даних у пам'яті
    connection = sqlite3.connect(':memory:')     #    Тимчасова база прямо в операційній памяті
    cursor = connection.cursor()                       #  вона зникає як тільки програма закривається

    # 2. Створення таблиць
    cursor.execute('''CREATE TABLE Salesmen (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        city TEXT)''')

    cursor.execute('''CREATE TABLE Customers (
                        id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        city TEXT)''')

    cursor.execute('''CREATE TABLE Sales (
                        id INTEGER PRIMARY KEY, 
                        amount REAL, 
                        sale_date DATE, 
                        salesman_id INTEGER, 
                        customer_id INTEGER,
                        FOREIGN KEY(salesman_id) REFERENCES Salesmen(id),
                        FOREIGN KEY(customer_id) REFERENCES Customers(id))''')

    # 3. Наповнення даними
    salesmen = [(1, 'Іван Іванов', 'Київ'), (2, 'Олена Петренко', 'Львів')]
    customers = [(101, 'Дмитро', 'Одеса'), (102, 'Анна', 'Київ')]
    sales = [
        (1, 5000, '2023-10-01', 1, 101),
        (2, 12000, '2023-10-02', 1, 102),
        (3, 3000, '2023-10-03', 2, 101),
        (4, 7500, '2023-10-04', 2, 102),
        (5, 1000, '2023-10-05', 1, 101)
    ]

    cursor.executemany("INSERT INTO Salesmen VALUES (?,?,?)", salesmen)
    cursor.executemany("INSERT INTO Customers VALUES (?,?,?)", customers)
    cursor.executemany("INSERT INTO Sales VALUES (?,?,?,?,?)", sales)

    # 4. Виконання запитів (функція-помічник)
    def print_query(title, query):
        print(f"\n--- {title} ---")
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    # Список усіх запитів згідно з завданням
    print_query("Усі угоди", "SELECT * FROM Sales")
    print_query("Угоди Івана (ID 1)", "SELECT * FROM Sales WHERE salesman_id = 1")
    print_query("Максимальна сума", "SELECT MAX(amount) FROM Sales")
    print_query("Мінімальна сума", "SELECT MIN(amount) FROM Sales")
    print_query("Макс. сума Івана", "SELECT MAX(amount) FROM Sales WHERE salesman_id = 1")
    print_query("Мін. сума Івана", "SELECT MIN(amount) FROM Sales WHERE salesman_id = 1")
    print_query("Макс. сума Дмитра (ID 101)", "SELECT MAX(amount) FROM Sales WHERE customer_id = 101")
    print_query("Мін. сума Дмитра", "SELECT MIN(amount) FROM Sales WHERE customer_id = 101")

    print_query("Продавець з макс. продажами",
                "SELECT salesman_id, SUM(amount) FROM Sales GROUP BY salesman_id ORDER BY SUM(amount) DESC LIMIT 1")

    print_query("Продавець з мін. продажами",
                "SELECT salesman_id, SUM(amount) FROM Sales GROUP BY salesman_id ORDER BY SUM(amount) ASC LIMIT 1")

    print_query("Покупець з макс. покупками",
                "SELECT customer_id, SUM(amount) FROM Sales GROUP BY customer_id ORDER BY SUM(amount) DESC LIMIT 1")

    print_query("Середній чек Дмитра", "SELECT AVG(amount) FROM Sales WHERE customer_id = 101")
    print_query("Середній чек Олени (ID 2)", "SELECT AVG(amount) FROM Sales WHERE salesman_id = 2")

    connection.close()


if __name__ == "__main__":
    run_sales_db()

"""
помагав друг і дивився шо ви писали і відео
"""