import sqlite3

conn = sqlite3.connect("playground.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        category TEXT,
        description TEXT,
        amount REAL
    )
""")

expenses = [
    ("2026-11-02", "Food", "Sandwich", 14.5),
    ("2026-11-02", "Drink", "Coffee", 5.5),
    ("2026-11-02", "Travel", "Plane Ticket", 444.5),
]

cur.executemany(
    "INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)",
    expenses,
)
conn.commit()

for row in cur.execute("SELECT * FROM expenses WHERE amount > 3"):
    print(row)

for row in cur.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category"):
    print(row)

for row in cur.execute("SELECT * FROM expenses ORDER BY amount DESC"):
    print(row)

conn.close()
