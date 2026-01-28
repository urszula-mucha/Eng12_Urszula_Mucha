#make a database of Monty Python movies with sqlite3

import sqlite3

my_connection = sqlite3.connect("Monty_Python_movies.db")
my_cursor = my_connection.cursor()

my_cursor.execute("CREATE TABLE IF NOT EXISTS movie(title TEXT UNIQUE, year INTEGER, score REAL)")
result = my_cursor.execute("SELECT name FROM sqlite_master")
result.fetchone()

my_cursor.execute("""INSERT OR IGNORE INTO movie VALUES
    ("MontyPython nd the Holy Grail", 1975, 8.2),
    ("And now for Something Completely Different", 1971, 7.5)
    """)

my_connection.commit()

result = my_cursor.execute("SELECT score FROM movie")
result.fetchall()

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]

my_cursor.executemany("INSERT OR IGNORE INTO movie VALUES(?, ?, ?)", data)
my_connection.commit()

my_cursor.execute("""
    DELETE FROM movie
    WHERE rowid NOT IN (
        SELECT MIN(rowid)
        FROM movie
        GROUP BY title
        )""")

for row in my_cursor.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

