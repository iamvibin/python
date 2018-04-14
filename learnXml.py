import xml.etree.ElementTree as ET
data = '''<person><name>Vibin</name><phone>+1 988 585 9800</phone><email hide ="yes"></email></person>'''

tree = ET.fromstring(data)
print('name :',tree.find('name').text)
print('Attr :',tree.find('email').get('hide'))

input = '''<stuff>
<users>
<user x="2">
<id>001</id>
<name>Lakhu</name>
</user>

<user x="2">
<id>007</id>
<name>Vibz</name>
</user>

</users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))
