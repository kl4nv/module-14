import sqlite3

# Связываемся с БД выполненной из прошлого ДЗ
connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

# 1
cursor.execute('DELETE FROM Users WHERE id = 6')

# 2
cursor.execute('SELECT COUNT (*) FROM Users')
total_count = cursor.fetchone()[0]

# 3
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# 4
print(all_balances/total_count)

# Альтернативный способ найти средний баланс
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()
