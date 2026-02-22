"""   Завдання 1
Створіть тритабличну базу даних Sales. У цій базі даних мають бути таблиці: Sales (інформація про конкретні продажі),
Salesmen (інформація про продавців), Customers (інформація про покупців).
Напишіть наступні запити

Відображення усіх угод;
Відображення угод конкретного продавця;
Відображення максимальної за сумою угоди;
Відображення мінімальної за сумою угоди;
Відображення максимальної суми угоди для конкретного продавця;
Відображення мінімальної за сумою угоди для конкретного продавця;
Відображення максимальної за сумою угоди для конкретного покупця;
Відображення мінімальної за сумою угоди для конкретного покупця;
Відображення продавця з максимальною сумою продажів за всіма угодами;
Відображення продавця з мінімальною сумою продажів за всіма угодами;
Відображення покупця з максимальною сумою покупок за всіма угодами;
Відображення середньої суми покупки для конкретного покупця;
Відображення середньої суми покупки для конкретного продавця."""


import sqlite3

conn = sqlite3.connect("sales.sqlite")
cur = conn.cursor()

cur.execute("PRAGMA foreign_keys = ON;")

# 1) створюємо таблиці і видаляємо старі - (IF EXISTS)

cur.executescript("""
DROP TABLE IF EXISTS Sales;
DROP TABLE IF EXISTS Salesmen;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Salesmen (
    salesman_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT,
    commission REAL
);

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    city TEXT,
    grade INTEGER
);

CREATE TABLE Sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sale_date TEXT,
    amount REAL NOT NULL,
    salesman_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    FOREIGN KEY (salesman_id) REFERENCES Salesmen(salesman_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
""")


cur.executescript("""
INSERT INTO Salesmen(name, city, commission) VALUES
('Ivan', 'Kyiv', 0.10),
('Olga', 'Lviv', 0.12);

INSERT INTO Customers(name, city, grade) VALUES
('Petro', 'Kyiv', 100),
('Anna', 'Odesa', 200);

INSERT INTO Sales(sale_date, amount, salesman_id, customer_id) VALUES
('2026-02-10', 1000, 1, 1),
('2026-02-11', 500,  1, 2),
('2026-02-11', 2000, 2, 1);
""")

conn.commit()

# 3) перевірка показати всі продажі
cur.execute("SELECT * FROM Sales;")   #    execute - запуск SQL
print(cur.fetchall())                           #   забирає всі рядки результату і в консоль

conn.close()


"""
Salemaen - продавці
salevan_id - унікальний номер продавця
cummission - комісія
Customers - покупці
customers_id - номер покупця
grade - число
REAL - число дробне
Sales - продажа
amount - угода суми
FOREIGN KEY - посилається на покупця чи продавця
 
"""