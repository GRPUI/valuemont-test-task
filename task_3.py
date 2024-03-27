import random
import sqlite3

from faker import Faker

conn = sqlite3.connect('identifier.sqlite')
cursor = conn.cursor()
fake = Faker()


def get_data() -> list:
    cursor.execute("SELECT name, last_name FROM employees "
                   "WHERE salary > 50000 "
                   "ORDER BY salary DESC "
                   "LIMIT 5")
    return cursor.fetchall()


def fill_data() -> None:
    cursor.execute("DROP TABLE IF EXISTS employees")
    cursor.execute("CREATE TABLE employees ("
                   "key INTEGER PRIMARY KEY, "
                   "name TEXT, "
                   "last_name TEXT, "
                   "salary INTEGER)")
    for i in range(1000):
        key = i
        name = fake.name().split(" ")
        salary = random.randint(100, 100000)
        cursor.execute(f"INSERT INTO employees "
                       f"VALUES (?, ?, ?, ?)",
                       (key, name[0], name[1], salary))
    conn.commit()


if __name__ == '__main__':
    fill_data()
    for i in get_data():
        print(i)
