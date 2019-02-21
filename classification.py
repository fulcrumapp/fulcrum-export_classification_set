def recursive(level, count):  
    array = []
    loop = count
    while loop > 0:
        array.append('')
        loop = loop - 1
    array.append(level['label'])
    array.append(level['value'])
    file.writerow(array)
    if('child_classifications' not in level):
        return
    else:
        count = count + 1
        for l in level['child_classifications']: 
            recursive(l, count)


import json
import csv

classFile = 'example.classes' # name of file. 
count = 0

with open(classFile, 'rt') as file:
    doc = file.read()

jsonData = json.loads(doc)
items = jsonData['items']
file = csv.writer(open("export.csv", "wb+"))

for item in items:
    recursive(item, count)
