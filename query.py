"""Запросы о статусе выполнения задачи"""
import sqlite3

conn = sqlite3.connect('test.db')  # связаться с базой данных test
cur = conn.cursor()  # объект курсора
cur.execute("SELECT * FROM users;")
ans = cur.fetchall()
while True:
    task = int(input('Введите идентификатор задачи: '))
    print(f'Статус выполнения задачи {ans[task - 1][0]} {ans[task - 1][3]}')
