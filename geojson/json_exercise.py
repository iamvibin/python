import urllib.parse, urllib.error, urllib.request
import json

url = input('Enter URL-')
handle = urllib.request.urlopen(url)
data = handle.read().decode()#UTF8  TO unicode 8
decodedData = json.loads(data)
comments = decodedData["comments"]
sum = 0
for comment in comments:
    sum = sum + int(comment["count"])
print(sum)
