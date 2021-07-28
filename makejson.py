import csv
import json

csvfile = open('pokemon_1.csv','r')
jsonfile = open('pokemon.json','w')

fieldnames = (
    "#","Name","Type 1",
    "Type 2","Total","HP",
    "Attack", "Defense", "Sp. Atk",
    "Sp. Def", "Speed", "Generation",
    "Legendary","hue","url"
)
reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row,jsonfile)
    jsonfile.write(',\n')
jsonfile.close()
