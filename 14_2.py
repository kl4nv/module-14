import sqlite3

# Связываемся с БД выполненной из прошлого ДЗ
cursor = sqlite3.connect('not_telegram.db').cursor()

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT (*) FROM Users')
all_count = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

print(all_balances/all_count)

# Альтернативный способ найти средний баланс
cursor.execute('SELECT AVG(balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)

cursor.close()