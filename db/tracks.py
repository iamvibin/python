import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''Drop Table if exists Artists;
                DROP TABLE IF EXISTS Album;
                DROP TABLE IF EXISTS Track;

                CREATE TABLE Artist(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
                );

                CREATE TABLE Genre(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
                );

                CREATE TABLE Album (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                artist_id Integer,
                title text unique
                );

                CREATE TABLE Track(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT UNIQUE,
                album_id INTEGER,
                genre_id INTEGER,
                LEN INTEGER,
                rating INTEGER,
                count INTEGER
                );
''')

fname = input('Enter the file name :')
if(len(fname) < 1) : fname = 'C:/Users/VIBIN/Desktop/pYmC3/db/Library.xml'

#The library.xml is dictionary of dictionary. for each child one has to
#iterate and check wether the track id is present or not
def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count :', len(all))

for entry in all:
    if(lookup(entry,'Track ID')) is None : continue

    name = lookup(entry,'Name')
    artist = lookup(entry,'Artist')
    genre = lookup(entry, 'Genre')
    album = lookup(entry,'Album')
    count = lookup(entry,'Play Count')
    rating = lookup(entry,'Rating')
    length = lookup(entry,'Total Time')

    if name is None or artist is None or album is None or genre is None:
        continue

    print(name,'|',artist,'|', genre,'|', album,'|', count,'|', rating,'|', length)
    #this is to insert an artist if not present or ignore if already there
    cur.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES (?)''', (artist, ))
    # takes the artist id which is the foreign key
    #and to be inserted in the album table
    cur.execute('Select id from Artist where name = ?', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', (genre,))
    cur.execute('Select id from Genre where name = ?', (genre, ))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (Title, artist_id)
        VALUES(?,?)''', (album,artist_id))
    cur.execute('Select id from Album where title = ?',(album, ))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title,album_id,genre_id,len,rating,count)
        VALUES(?,?,?,?,?,?)''',(name, album_id, genre_id, length, rating, count))

conn.commit()
