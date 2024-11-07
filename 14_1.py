import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                     (f'User{i}', f'example{i}@gmail.ru', i * 10, 1000))

cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', (500,))

del_set = ()
for i in range(1, 11, 3):
    del_set += (i, )

cursor.execute(f'DELETE FROM Users WHERE id IN {str(del_set)}')

cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()

for user in users:
    if 60 not in user:
        print(f'Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}')

connection.commit()
connection.close()
