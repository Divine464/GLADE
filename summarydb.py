
import sqlite3

def get_summary_data(username):
    income_conn = sqlite3.connect("data.db")
    income_cursor = income_conn.cursor()

    income_cursor.execute("SELECT SUM (amount) FROM incomes WHERE username = ?",(username,))
    total_income = income_cursor.fetchone()[0]
    if total_income is None:
          total_income = 0

    income_cursor.execute("SELECT amount,date FROM incomes WHERE username = ? ORDER BY id DESC LIMIT 1",(username,))
    last_income = income_cursor.fetchone()
    if not last_income:
          last_income = ("None","N/A")

    income_conn.close()



    expense_conn = sqlite3.connect("expenses.db")
    expense_cursor = expense_conn.cursor()


    expense_cursor.execute("SELECT SUM (amount) FROM expenses WHERE username = ?",(username,))
    total_expenses = expense_cursor.fetchone()[0]
    if total_expenses is None:
          total_expenses = 0

    expense_cursor.execute("SELECT amount,date FROM expenses WHERE username = ? ORDER BY id DESC LIMIT 1",(username,))
    last_expense = expense_cursor.fetchone()
    if not last_expense:
          last_expense = ("None","None")

    expense_conn.close()


    balance = total_income - total_expenses

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance,
        "last_income": last_income,
        "last_expense": last_expense
    }


        


    