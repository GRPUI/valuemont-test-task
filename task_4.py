import sqlite3

conn = sqlite3.connect('identifier.sqlite')
cursor = conn.cursor()


def get_data() -> list:
    cursor.execute("SELECT salary FROM employees "
                   "WHERE salary = (SELECT salary FROM employees GROUP BY salary ORDER BY salary DESC LIMIT 1 OFFSET 1) "
                   "LIMIT 1;")
    return cursor.fetchall()


if __name__ == '__main__':
    print(get_data())
