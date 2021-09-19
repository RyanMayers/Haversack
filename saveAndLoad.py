import json
import character

saveFile = 'saveData.json'

def charToDict(j):
    data = {
        "ID": 0,
        "name": j.name,
        "gameClass": j.gameClass,
        "stats": [j.str,j.dex,j.con,j.int,j.wis,j.cha],
        "profList": j.proficiencies,
        "level": j.level,
        "favColor": j.favColor,
        "wealth": j.rawWealth
    }
    return data

def saveChar(j):
    save = charToDict(j)
    with open(saveFile, 'w') as file:
        json.dump(save, file)

def loadChar(id):
    with open(saveFile) as file:
        d = json.load(file)
    loaded = character.Character(d["name"], d["gameClass"], d["stats"], d["profList"], d["level"], d["favColor"], d["wealth"])
    print(f"Loaded character: {loaded.pname}")
    return loaded