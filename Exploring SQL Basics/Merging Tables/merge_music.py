
import sqlite3

db_a = sqlite3.connect('music.sqlite')
db_b = sqlite3.connect('music_2.sqlite')

b_cur = db_b.cursor()
b_cur.execute('SELECT * FROM Blah')
output = b_cur.fetchall()

a_cur = db_a.cursor()
for row in output:
    list_row = list(row)
    trackID_count = list_row[0]
    list_row[0] = trackID_count + 3
    row = (list_row)
    a_cur.execute('INSERT INTO Tracks VALUES (?, ?, ?)', row)
    
db_a.commit()
db_a.close()
db_b.close()
