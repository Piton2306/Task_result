"""Выполнение задачи"""
import time
import sqlite3

conn = sqlite3.connect('test.db')  # связаться с базой данных test
cur = conn.cursor()  # объект курсора
cur.execute("SELECT * FROM users;")  # выполнить команду для извлечения всех данных из таблицы users
ans = cur.fetchall()  # сохранить все извлеченные данные в переменной ans
print('Запуск выполнения задач')
for i in ans:
    if i[3] == 'Выполнено':
        continue
    num = i[0]
    conn.execute(f"UPDATE users SET Статус ='Выполняется' WHERE id = {num}")
    conn.commit()
    print(f'Задача с идентификатором {num} выполняется')
    if i[2] == 'Выполнить разворот строки':
        time.sleep(2)
        rev = i[1][::-1]
        conn.execute("UPDATE users SET 'Данные' = ? WHERE id = ?", (rev, num))
        conn.commit()
    elif i[2] == 'Выполнить попарно перестановку четных и нечетных символов в строке':
        time.sleep(5)
        a = i[1]
        task = []
        for i in range(0, len(a), 2):
            try:
                task.append(a[i + 1])
                task.append(a[i])
            except:
                task.append(a[len(a) - 1])
                break
        task_str = ''.join(task)

        conn.execute("UPDATE users SET 'Данные' = ? WHERE id = ?", (task_str, num))
        conn.commit()
    elif i[2] == 'Выполнить повтор символа в строке согласно его позиции':
        time.sleep(7)
        a = i[1]
        task1 = []
        for i in range(len(a)):
            task1.append((i + 1) * a[i])
        task1_str = "".join(task1)
        conn.execute("UPDATE users SET 'Данные' = ? WHERE id = ?", (task1_str, num))
        conn.commit()
    conn.execute(f"UPDATE users SET Статус ='Выполнено' WHERE id = {num}")
    conn.commit()
print("Все задачи выполнены")
