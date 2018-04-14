import json
data = '''{
    "name" : "Chuck",
    "phone":{
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
"email" : {
    "hide" : "yes"
    }
}'''
info = json.loads(data)# PYTHON DICTIONARY
print('Name:',info["name"])#INFO IS DICTIONARY
print('Hide:',info["email"]["hide"])#

INPUT = '''[
    { "id:" : "009",
      "x" : "7",
      "name" : "vibz"
    },
    { "id:" : "001",
      "x" : "6",
      "name" : "laksh"
    }
]'''

info = json.loads(INPUT)# return a list of dictionaries
print('user Count', len(info))
for item in info:
    print('Name', item['name'])
    print('Id',item['id:'])
    print('Attribute', item['x'])
