
from kivymd.toast import toast
import sqlite3


def connect_db():
    return sqlite3.connect("data.db")


def create_income_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incomes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
        )  
    """)
    conn.commit()
    conn.close()

def insert_income(username,amount, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO incomes (username,amount, date) VALUES (?,?,?)",
                        (username,amount, date))
    conn.commit()
    conn.close()

def fetch_all_incomes(username):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id,amount, username, date FROM incomes WHERE username = ?",(username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_income(income_id, amount, date):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
            UPDATE incomes
            SET amount = ?,date = ? WHERE id = ?
""", (amount, date, income_id))
    conn.commit()
    conn.close()

def delete_income(income_id):
    print("TRYING TO DELETE")
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM incomes WHERE id = ? ", (int(income_id),))
    conn.commit()
    conn.close()
