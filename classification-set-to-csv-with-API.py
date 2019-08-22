# -*- coding: utf-8 -*-
import json
import csv
import sys
import getopt
import argparse
from fulcrum import Fulcrum


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


parser = argparse.ArgumentParser(description='This program takes a classification set from the API and turns it into a csv file.')
parser.add_argument('-t','--token', help='API token', required=True)
parser.add_argument('-cs','--classSetId', help='ID of classification set', required=True)
args = vars(parser.parse_args())

token = args['token'] # fulcrum API token
classId = args['classSetId'] # classification set id
fulcrum = Fulcrum(key=token)
classSet = fulcrum.classification_sets.find(classId)
count = 0

#jsonData = json.loads(classSet)
items = classSet['classification_set']['items']
file = csv.writer(open("export.csv", "w+"))

for item in items:
    recursive(item, count)