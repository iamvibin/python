import urllib.parse, urllib.error, urllib.request
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('friends.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS People (id INTEGER PRIMARY KEY,name TEXT UNIQUE, retrieved INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS Follows (from_id INTEGER ,to_id INTEGER, UNIQUE(from_id, to_id))')

#IGNORE SSL CERTIFICATE
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter the Twitter Account or quit :')
    if (acct == 'quit'): break
    if(len(acct) < 1):
        cur.execute('SELECT id, name from People where retrieved = 0 LIMIT 1')
        try:
            (id,acct) = cur.fetchone()
        except:
            print('No unretrieved Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id from People where name = ? LIMIT 1', (acct,))
        try:
            id = cur.fetchone()
        except:
            cur.execute('INSERT OR IGNORE INTO People (name, retrieved) VALUES (?,0)',(acct,))
            conn.commit()
            if cur.rowcount !=1:
                print('Error in inserting acount:',acct)
                continue
            id = cur.lastrowid

        url = twurl.augment(TWITTER_URL, {'screen_name':acct, 'count': '100'})
        print('Retrieving',url)
        connection = urlopen(url, context = ctx)
        data = connection.read().decode()#read gives in UTF-8 and decode converts it into unicode
        headers = dict(connection.getheaders())

        print('Reamining attempts', headers['x-rate-limit-remaining'])

        try:
            js = json.loads(data)
        except:
            print('Unable to parse json')
            print(data)
            break


        if 'users' not in js:
            print('Incorrect JSON RECEIVED')
            print(json.dump(js, indent =4))
            continue

        # Retrived is now set to one for the acct we are using
        cur.execute('UPDATE People SET retrieved=1 WHERE name=?', (acct,))

        countnew = 0
        countold = 0

        for u in js['users']:
            friend = u['screen_name']
            print(friend)
            cur.execute('SELECT friends FROM People where name = ? LIMIT 1', (friend,))


            try:
                friend_id = cur.fetchone()[0]
                countold = countold + 1

            except:
                cur.execute('INSERT or ignore INTO People (name, retrieved) VALUES (?, 0)', (friend,))
                conn.commit()
                if cur.rowcount !=1:
                    print('Error inserting the account:', friend)
                    continue
                friend_id = cur.lastrowid
                countnew = countnew + 1
            cur.execute('''INSERT OR IGNORE INTO Follows (from_id, to_id) VALUES (?,?)''',(ID, friend_id))

        print('NEW ACCOUNTS = ', countnew, ' revisited=', countold)
        conn.commit()
cur.close()
