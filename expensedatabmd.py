

import sqlite3


def init_expense_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        username TEXT NOT NULL
        )  
    """)
    conn.commit()
    conn.close()

def insert_expense( amount, description, category, date, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, description, category, date, username) VALUES (?,?,?,?,?)",
                        (amount, description, category, date, username))
    conn.commit()
    conn.close()

def get_all_expenses(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses WHERE username = ?", (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_expense(expense_id,amount, description, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE expenses
                   SET amount = ?, description = ?, category = ?, date = ? WHERE id = ?""",
                   (amount, description, category, date, expense_id))
    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    conn.close()

