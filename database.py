import sqlite3

conn = sqlite3.connect("maindatabase.db")
print ("Database opened successfully!")

with open('schema.sql') as f:
    conn.executescript(f.read())

# cur = conn.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

# cur.executemany("INSERT INTO units VALUES(?, ?, ?);", 
#                 [
#                     ("Longbowman", "Britons", 100),
#                     ("Huskarl", "Goths", 120),
#                     ("Militia", None, 40)
#                 ])

conn.commit()
conn.close()

