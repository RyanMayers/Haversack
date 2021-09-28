import os
import json

directory = '/Users/ryanmayers/Documents/Haversack/gather spells/spellsJSON/'

indices = []

for f in os.listdir(directory):
    if f.endswith('.json') and f != 'SpellCatalog.json':
        indices.append(f)

indices.sort()

with open("listspells2.txt", mode="w") as file:
    for g in indices:
        h = open(directory+g)
        i = json.load(h)
        h.close()
        file.write(i['name']+"\n")
    file.close()