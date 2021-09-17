import Spell
import requests, json
import rolldice as d
import ability
# url = "https://www.dnd5eapi.co/api/spells/"
# jsonAllSpells = requests.request("GET", url).json()
# spellList = []
# for i in jsonAllSpells["results"]:
#     spellList.append(i["index"])
# for i in spellList:
#     Spell.printSpell(i)

# https://github.com/Fiona1729/py-rolldice found a dice library

# class Character:
#     def __init__(self, file):
        
glyn = ability.Character("Glynlamin",  [16,8,15,10,18,7], 3, ["Perception", "Insight", "Survival"], "GREEN")

print(glyn.check("wis"))