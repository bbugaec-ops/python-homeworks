import sqlite3
import random

def main():
    conn = sqlite3.connect("test_db.sqlite")
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    cursor.executescript("""
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS products;

        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            price NUMERIC NOT NULL CHECK (price >= 0),
            stock INTEGER NOT NULL CHECK (stock >= 0)
        );

        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            total_price NUMERIC NOT NULL,
            order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE
        );
    """)

    cursor.executemany(
        "INSERT INTO products (name, price, stock) VALUES (?, ?, ?);",
        [
            ("iphone 15", 600, 10),
            ("iphone 16", 700, 10),
            ("iphone 17", 800, 10),
            ("iphone 18", 900, 10),
        ],
    )
    conn.commit()

    model_id = random.randint(1, 4)

    cursor.execute("SELECT price FROM products WHERE id = ?;", (model_id,))
    product_price = cursor.fetchone()[0]

    quantity = random.randint(1, 10)
    total_price = product_price * quantity

    cursor.execute(
        "INSERT INTO orders (product_id, quantity, total_price) VALUES (?, ?, ?);",
        (model_id, quantity, total_price),
    )
    conn.commit()

    cursor.execute("SELECT * FROM products;")
    for row in cursor.fetchall():
        print(row)

    cursor.execute("SELECT * FROM orders;")
    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
