This file marks where my SQL journey began.

*Note: The full .py files can be found in the folders with the same name as the headers in this file.*

# Table of Contents

* [The 4 Basic Commands](#The-4-Basic-Commands)
* [Merging Tables](#Merging-Tables)

# The 4 Basic Commands

This file shows my first attempt at the 4 basic SQL commands - create, insert, where, delete. 

```python
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
```

This produces the following table:  
![](https://github.com/ezhentan/schoolprojects/blob/master/Exploring%20SQL%20Basics/The%204%20Basic%20Commands/Images/DB%20Browser%201.png)

```python
# reading the database
## selecting different columns
print('Tracks: ')
cur.execute('SELECT * FROM Tracks') #selecting all columns to display
for row in cur:
    print(row)
print('----------------------------------------')
```

Terminal result:  


![](https://github.com/ezhentan/schoolprojects/blob/master/Exploring%20SQL%20Basics/The%204%20Basic%20Commands/Images/Terminal%203.png)

```python
print('Tracks: ')
cur.execute('SELECT title FROM Tracks')
for row in cur:
    print(row)
print('----------------------------------------')
```

Terminal result:


![](https://github.com/ezhentan/schoolprojects/blob/master/Exploring%20SQL%20Basics/The%204%20Basic%20Commands/Images/Terminal%202.png)

```python    
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
```
The result: 
![In DB Browser for SQLite](https://github.com/ezhentan/schoolprojects/blob/master/Exploring%20SQL%20Basics/The%204%20Basic%20Commands/Images/DB%20Browser%204.png)

**Tutorial followed:**

Severance, Charles (2016, July 5). Python For Everybody: Exploring Data Using Python 3. Retrieved from: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf

# Merging Tables

```python
import sqlite3

db_a = sqlite3.connect('music.sqlite')
db_b = sqlite3.connect('music_2.sqlite')

b_cur = db_b.cursor()
b_cur.execute('SELECT * FROM Blah')
output = b_cur.fetchall()

a_cur = db_a.cursor()
for row in output:
    list_row = list(row) #converting to list as tuples are immutable
    list_row[0] = list_row[0] + 3
    row = (list_row)
    a_cur.execute('INSERT INTO Tracks VALUES (?, ?, ?)', row)
    
db_a.commit()
db_a.close()
db_b.close()
```

Result:

![](https://github.com/ezhentan/schoolprojects/blob/master/Exploring%20SQL%20Basics/The%204%20Basic%20Commands/Images/DB%20Browser%203.png)
