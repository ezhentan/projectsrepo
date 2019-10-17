import sqlite3

conn = sqlite3.connect('music_2.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Blah')
cur.execute('CREATE TABLE Blah (track_ID INTEGER PRIMARY KEY, title TEXT, plays INTEGER)')

cur.execute('INSERT INTO Blah (title, plays) VALUES (?, ?)', ('Barney song', 1))
cur.execute('INSERT INTO Blah (title, plays) VALUES (?, ?)', ('Only one', 3))

conn.commit()

conn.close()

