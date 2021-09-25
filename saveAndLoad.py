import json
import character

saveFile = 'saveData.json'

def charToDict(j):
    index = 0
    data = {
        index: {
            "name": j.name,
            "gameClass": j.gameClassName,
            "stats": [j.str,j.dex,j.con,j.int,j.wis,j.cha],
            "profList": j.proficiencies,
            "level": j.level,
            "favColor": j.favColor,
            "wealth": j.rawWealth,
            "inventory": j.inventory
        }
    }
    return data

def saveChar(j):
    save = charToDict(j)
    with open(saveFile, 'w') as file:
        json.dump(save, file)
        file.close

def loadChar(index):
    with open(saveFile) as file:
        d = json.load(file)[str(index)]
        file.close
    loaded = character.Character(d["name"], d["gameClass"], d["stats"], d["profList"], d["level"], d["favColor"], d["wealth"], d["inventory"])
    print(f"Loaded character: {loaded.pname}")
    return loaded

def listSaved():
    with open(saveFile) as file:
        d = json.load(file)
        file.close
    iters = len(d.keys()) - 1
    index = 0
    response = []
    while iters >= 0:
        row = d[str(index)]
        response.append(f"[{index+1}]: {row['name']}, Level {row['level']} {row['gameClass']}")
        iters -= 1
        index += 1
    return response