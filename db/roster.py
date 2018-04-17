import json
import sqlite3

conn =sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member(
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id,course_id)
);

''')

fname = 'C:/Users/VIBIN/Desktop/pYmC3/db/roster_data.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print(name,'|',title,'|',role)
    if name is None or title is None or role is None:
        continue
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)',(name, ))
    cur.execute('INSERT OR IGNORE INTo Course (title) VALUES (?)',(title, ))

    cur.execute('Select id from User where name = ?', (name,))
    user_id = cur.fetchone()[0]
    cur.execute('Select id from Course where title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('Insert or REPLACE into Member (user_id,course_id,role) VALUES (?,?,?)',(user_id,course_id,role))

conn.commit()
