import sqlite3

import connection

conn = sqlite3.connect('ps.db')

cursor=conn.cursor()

# Створюємо таблицю Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER)''')

# Додаємо новий запис до таблиці
cursor.execute("INSERT INTO Users (username, email, age) VALUES ('newuser3', 'newuser3@example.com', 28)")

res = cursor.execute("SELECT * FROM Users")

for row in res.fetchall():
    print(row)


conn.commit()
conn.close()
