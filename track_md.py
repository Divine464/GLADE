# # # To check for users input data
# import sqlite3

# conn = sqlite3.connect("users.db")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# conn.close()

# # # conn = sqlite3.connect("expenses.db")
# # # cursor = conn.cursor()
# # # cursor.execute("SELECT * FROM expenses")
# # # raws = cursor.fetchall()

# # # for raw in raws:
# # #     print(raw)

# # # conn.close()


# # # To deleted users info
# # # import sqlite3
# # #
# # # conn = sqlite3.connect("users.db")
# # # cursor = conn.cursor()
# # # cursor.execute("DELETE FROM users")
# # # conn.commit()
# # #
# # # print("All user data deleted")
# # # conn.close()

# # # import os

# # # if os.path.exists("data.db"):
# # #     os.remove("data.db")
# # #     print("Database deleted")
# # # else:
# # #     print("Database file not found")

# # import kivymd
# # print(kivymd.__version__)

