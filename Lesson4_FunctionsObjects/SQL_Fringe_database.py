#database of Fringe episodes with sqlite3

import sqlite3

my_connection = sqlite3.connect("Fringe_episodes.db")
my_cursor = my_connection.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS episode(title TEXT UNIQUE, season INTEGER, word TEXT UNIQUE)")
result = my_cursor.execute("SELECT name FROM sqlite_master")
result.fetchone()

my_cursor.execute("""INSERT OR IGNORE INTO episode VALUES
    ("The Arrival", 1, "ROGUE"),
    ("Power Hungry", 1, "SURGE")
    """)

my_connection.commit()

result = my_cursor.execute("SELECT word FROM episode")
result.fetchall()

data = [
    ("Pilot", 1, "OBSERVER"),
    ("The Same Old Story", 1, "CHILD"),
    ("The Ghost Network", 1, "AEGER"),
]

my_cursor.executemany("INSERT OR IGNORE INTO episode VALUES(?, ?, ?)", data)
my_connection.commit()

for row in my_cursor.execute("SELECT word, title FROM episode ORDER BY word"):
    print(row)

