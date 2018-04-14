import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/l.l/friends/list.json'

while True:
    print('')
    acct = input('Enter Twitter Account')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url)
    data = connection.read().decode()

    #urllib does not take getheaders
    #to get the headers in form of dictionary
    headers = dict(connection.getheaders())

    #No of connections atempts per day
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)

    #print the json in a more representative way
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50])
