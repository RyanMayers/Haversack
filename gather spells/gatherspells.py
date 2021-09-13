import requests, json
url = "https://www.dnd5eapi.co/api/spells/"
jsonAllSpells = requests.request("GET", url).json()
spellList = []
for i in jsonAllSpells["results"]:
    spellList.append(i["index"])
def spellAPI(spell):
    return requests.request("GET", url + spell).json()
for j in spellList:
    data = spellAPI(j)
    spellID = data["index"]
    name = data["name"]
    with open(f'./spellsJSON/{spellID}.json', "w") as out:
        print(f'Writing {name}...')
        json.dump(data, out, indent = 4)
        out.close()