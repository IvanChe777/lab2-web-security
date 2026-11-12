
import sqlite3

DB_NAME = "shop.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM products")

    if cursor.fetchone()[0] == 0:
        products = [
            ("Ноутбук", 55000),
            ("Мышка", 1200),
            ("Клавиатура", 2500),
            ("Монитор", 18000),
            ("Наушники", 3500)
        ]

        cursor.executemany(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            products
        )

    conn.commit()
    conn.close()
