import sqlite3
import random
from faker import Faker

conn = sqlite3.connect('identifier.sqlite')
cursor = conn.cursor()
fake = Faker()


def fill_data() -> None:
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("CREATE TABLE transactions ("
                   "user_id INTEGER, "
                   "amount INTEGER, "
                   "timestamp TIMESTAMP)")
    user_ids = [i for i in range(100)]
    for i in range(1000):
        user_id = random.choice(user_ids)
        amount = random.randint(1, 300)
        time = fake.date_time_this_year()
        cursor.execute(f"INSERT INTO transactions "
                       f"VALUES (?, ?, ?)",
                       (user_id, amount, time))
    conn.commit()


def get_data() -> list:
    cursor.execute("""SELECT user_id 
FROM transactions
WHERE timestamp >= date('now','-1 month')
GROUP BY user_id
HAVING SUM(amount) > 1000;
""")
    return cursor.fetchall()


if __name__ == '__main__':
    fill_data()
    for i in get_data():
        print(i)
