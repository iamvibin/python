import urllib.parse , urllib.error, urllib.request
from bs4 import BeautifulSoup

url = input('Enter the link -')
count = input('Enter Count -')
position = input('Enter Position -')
#bs4 has lxml and other parsers too!!!

for i in range(int(count)):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    number = 0
    for tag in tags:
        number = number + 1
        if number == int(position):
            url = tag.get('href')
            break
print(tag.contents[0])
#print(tag.contents[1])
