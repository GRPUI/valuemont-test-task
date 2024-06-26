import sqlite3

conn = sqlite3.connect('identifier.sqlite')
cursor = conn.cursor()


def get_data() -> list:
    cursor.execute("SELECT salary FROM employees GROUP BY salary ORDER BY salary DESC LIMIT 1 OFFSET 1")
    return cursor.fetchone()


if __name__ == '__main__':
    print(get_data())
