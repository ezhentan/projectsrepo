import sqlite3

conn = sqlite3.connect('music.sqlite') #will create the file if doesn't already exists
cur = conn.cursor()

# creating the database
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (track_ID INTEGER PRIMARY KEY, title TEXT, plays INTEGER)')

# adding things into table
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('My Way', 15))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', ('All with you', 100))
conn.commit() # writing out the changes to disc, write every 10th record, for e.g.

# reading the database
## selecting different columns
print('Tracks: ')
cur.execute('SELECT * FROM Tracks') #selecting all columns to display
for row in cur:
    print(row)
print('----------------------------------------')

print('Tracks: ')
cur.execute('SELECT title FROM Tracks')
for row in cur:
    print(row)
print('----------------------------------------')
    
print('Tracks: ')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
    print(row)
    
print('----------------------------------------')

## using 'WHERE'
cur.execute('SELECT * FROM Tracks WHERE title = "My Way"') #selecting a track by title
for row in cur:
    print(row)

print('----------------------------------------')

cur.execute('SELECT title, plays FROM Tracks ORDER BY title')
for row in cur:
    print(row)
    
print('----------------------------------------')

## using 'DELETE'
cur.execute('DELETE FROM Tracks WHERE title = "My Way"')
cur.execute('SELECT * FROM Tracks')
for row in cur:
    print(row)

print('----------------------------------------')

## using 'UPDATE'
track_title = 'Thunderstruck'
cur.execute('SELECT * FROM Tracks WHERE title = ?', (track_title, ))
for row in cur:
    play_count = row[2]
    cur.execute('UPDATE Tracks SET plays = ? WHERE title = ?', (play_count + 1, track_title))

conn.commit()

conn.close()

#good to use 'update' command for changes in one cell
