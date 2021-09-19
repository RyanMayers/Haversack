import Spell
import requests, json
import rolldice as d
import ability
import character
import saveAndLoad as sl

# self, name, gameclass, stats: list, profList: list, level = 1, favColor = "GREEN", wealth = 0
glyn = character.Character(name="Glynlamin", gameclass="Druid",  stats=[16,8,15,10,18,7], profList=["Perception", "Insight", "Medicine", "Religion"], level = 4, favColor = "GREEN")

print(sl.charToDict(glyn))

# sl.saveChar(glyn)

# sl.loadChar(0)