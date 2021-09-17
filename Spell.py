import requests
import pprint
import json
import sqlite3
import inflect

p = inflect.engine()

# class Spell:
#     "A spell is a discrete magical effect, a single shaping of the magical energies that suffuse the multiverse into a specific, limited expression. In casting a spell, a character carefully plucks at the invisible strands of raw magic suffusing the world, pins them in place in a particular pattern, sets them vibrating in a specific way, and then releases them to unleash the desired effect—in most cases, all in the span of seconds."
#     def __init__(self, name, school, level, dndClass, castingTime, spellRange, components, duration, desc):
#         self.name = name
#         self.school = school
#         self.dclass = dndClass
#         self.level = level
#         self.time = castingTime
#         self.range = spellRange
#         self.comp = components
#         self.dur = duration
#         self.desc = desc

# class Spell:
#     "A spell is a discrete magical effect, a single shaping of the magical energies that suffuse the multiverse into a specific, limited expression. In casting a spell, a character carefully plucks at the invisible strands of raw magic suffusing the world, pins them in place in a particular pattern, sets them vibrating in a specific way, and then releases them to unleash the desired effect—in most cases, all in the span of seconds."
#     def __init__(self, spellID):
#         data = spellLookup(spellID)
#         self.casting_time = casting_time
#         self.classes = classes
#         self.components = components
#         self.concentration = concentration
#         self.desc = desc
#         self.duration = duration8u
#         self.index = index
#         self.level = level
#         self.material = material
#         self.name = name
#         self.castrange = castrange
#         self.ritual = ritual
#         self.school = school
#         self.subclasses = subclasses
#         self.url = url

# Spell Scroll is for holding a newly collected spell. Key is name, value is Spell opject.
spellScroll = {
    'index': '',
    'name': '',
    'desc': [],
    'higher_level': [],
    'range': '',
    'components': [],
    'material': '',
    'ritual': False,
    'duration': '',
    'concentration': False,
    'casting_time': '',
    'level': 0,
    'attack_type': '',
    'damage': '',
    'school': '',
    'classes': [],
    'subclasses': [],
    'url': ''
}

headers = [
    "index", 
    "name", 
    "desc", 
    "higher_level", 
    "range", 
    "components", 
    "material", 
    "ritual", 
    "duration", 
    "concentration", 
    "casting_time", 
    "level", 
    "attack_type", 
    "damage", 
    "school", 
    "classes", 
    "subclasses", 
    "url"
]

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def spellLookup(spell):
    directory = f"./gather spells/spellsJSON/{spell}.json"
    with open(directory) as file:
        data = json.load(file)
        file.close()
    return data

def printSpell (spell):
    data = spellLookup(spell)
    print("\n\n" + color.BOLD + color.RED + data["name"] + color.END + "\n")
    print(color.UNDERLINE + p.ordinal(data["level"]) + "-level " + data["school"]["index"] + " spell" + color.END + "\n")
    desc = "\n\n".join(data["desc"])
    comp = ", ".join(data["components"])
    if "higher_level" in data:
        hl = "\n\n".join(data["higher_level"])
    else:
        hl = ""
    print("Casting Time: " + data["casting_time"])
    print("Range:        " + data["range"])
    print("Components:   " + comp)
    print("Duration:     " + str(data["duration"]) + "\n\n")
    print(color.UNDERLINE + "Description:\n\n" + color.END + desc + hl)