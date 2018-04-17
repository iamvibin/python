import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()#cursor is the handle in which sql commands are sent through to get results

cur.execute(' Drop table if exists Counts')

cur.execute('CREATE TABLE Counts (org TEXT, Count Integer)')

fname = input('Enter the file name:-')
if(len(fname)< 1): fname = 'C:/Users/VIBIN/Desktop/pYmC3/db/mbox-short.txt'


fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    orgs = pieces[1].split('@')
    org = orgs[1]
    cur.execute('Select count from Counts where org = ?', (org,))
    row = cur.fetchone()

    if row is None:
        cur.execute('Insert into Counts (org,count) values (?, 1)',(org,))
    else:
        cur.execute('Update Counts Set Count = Count +1 where org = ?',(org,))

conn.commit()

sqlstr = 'select org,count from Counts order by COUNT DESC '

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
