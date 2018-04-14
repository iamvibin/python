import urllib.parse, urllib.error, urllib.request
import json
#in the docementation
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input("Rnter the location: ")
    if len(address) < 1:break


    url = serviceurl + urllib.parse.urlencode({'address': address})
    print(url)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()#UTF8  TO unicode 8
    print('Retrieved', len(data), 'charachters')


    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('***** Failure to Retrieve *****')
        print(data)
        continue

    print(js["results"][0]['place_id'])
