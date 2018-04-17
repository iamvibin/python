import urllib.parse, urllib.error, urllib.request
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('spider.sqlite')
cur = conn.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS Twitter (name TEXT, retrieved INTEGER, friends INTEGER )')

#IGNORE SSL CERTIFICATE
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter the Twitter Account or quit :')
    if (acct == 'quit'): break
    if(len(acct) < 1):
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1')
        try:
            acct = cur.fetchone()[0]
        except:
            print('No unretrieved Twitter accounts found')
            continue

        url = twurl.augment(TWITTER_URL, {'screen_name':acct, 'count': '5'})
        print('Retrieving',url)
        connection = urlopen(url, context = ctx)
        data = connection.read().decode()#read gives in UTF-8 and decode converts it into unicode
        headers = dict(connection.getheaders())

        print('Reamining attempts', headers['x-rate-limit-remaining'])
        js = json.loads(data)


        # Retrived is now set to one for the acct we are using
        cur.execute('UPDATE Twitter SET retrieved=1 WHERE name=?', (acct,))

        countnew = 0
        countold = 0

        for u in js['users']:
            friend = u['screen_name']
            print(friend)
            cur.execute('SELECT friends FROM Twitter where name = ? LIMIT 1', (friend,))
            countold = countold + 1

            try:
                count = cur.fetchone()[0]
                cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?', (count+1, friend))
                countold = countold + 1
            except:
                cur.execute('INSERT INTO Twitter (name, retrieved, friends) VALUES (?, 0, 1)', (friend,))
                countnew = countnew + 1

        print('NEW ACCOUNTS = ', countnew, ' revisited=', countold)
        conn.commit()
cur.close()
