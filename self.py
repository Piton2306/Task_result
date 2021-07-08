"""Добавление данных в БД"""
import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   id INTEGER PRIMARY KEY,
   Данные TEXT,
   Тип_задачи TEXT,
   Статус TEXT);
""")
conn.commit()
while True:
    user = input('Введите данные:'), input("Тип задачи:Выполнить разворот строки \n Выполнить попарно перестановку четных и нечетных символов в строке \n Выполнить повтор символа в строке согласно его позиции \n"), 'в очереди'
    cur.execute("INSERT INTO users(Данные,Тип_задачи, Статус) VALUES(?,?,?);", user)

    conn.commit()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY id DESC LIMIT 1;")
    three_results = cur.fetchone()
    print(f'Задача с идентификатором {three_results[0]} добавлена')
