# -*- coding: utf-8 -*-
import json
import csv
import sys
import getopt


def recursive(level, count):  
    array = []
    loop = count
    while loop > 0:
        array.append('')
        loop = loop - 1
    array.append(level['label'].encode('utf-8'))
    array.append(level['value'].encode('utf-8'))
    file.writerow(array)
    if('child_classifications' not in level):
        return
    else:
        count = count + 1
        for l in level['child_classifications']: 
            recursive(l, count)


fullCmdArguments = sys.argv

classFile = fullCmdArguments[2] # name of file. 
count = 0

with open(classFile, 'rt') as file:
    doc = file.read()

jsonData = json.loads(doc)
items = jsonData['items']
file = csv.writer(open("export.csv", "wb+"))

for item in items:
    recursive(item, count)
