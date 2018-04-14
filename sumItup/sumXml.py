import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

url = input('ENTER THE URL -')
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)

#print(tree.find('commentinfo').text)
lst = tree.findall('.//count')
sum = 0
print(len(lst))
for c in lst:
    print(c.text)
    sum = sum + int(c.text)

print(sum)
