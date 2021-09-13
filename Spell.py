import requests
import pprint
import json
import sqlite3

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

class Spell:
    "A spell is a discrete magical effect, a single shaping of the magical energies that suffuse the multiverse into a specific, limited expression. In casting a spell, a character carefully plucks at the invisible strands of raw magic suffusing the world, pins them in place in a particular pattern, sets them vibrating in a specific way, and then releases them to unleash the desired effect—in most cases, all in the span of seconds."
    def __init__(self, casting_time, classes, components, concentration, desc, duration, index, level, material, name, castrange, ritual, school, subclasses, url):
        self.casting_time = casting_time
        self.classes = classes
        self.components = components
        self.concentration = concentration
        self.desc = desc
        self.duration = duration
        self.index = index
        self.level = level
        self.material = material
        self.name = name
        self.castrange = castrange
        self.ritual = ritual
        self.school = school
        self.subclasses = subclasses
        self.url = url

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

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1

def getSpell(j, database):
    k = j.replace(' ', '-')
    spellName = k.lower()
    print(f"\nGetting {spellName} from D&D 5e API...")
    spellsUrl = "https://www.dnd5eapi.co/api/spells/"
    response = requests.request("GET", spellsUrl + spellName)
    data = json.loads(response.text)
    for l in [*data]:
        spellScroll[l] = data[l]
    lists = ["desc", "higher_level", "components"]
    for m in lists:
        spellScroll[m] = listToString(spellScroll[m])
    objects = ["damage", "school", "classes", "subclasses"]
    for n in objects:
        spellScroll[n] = str(spellScroll[n])
    dataForTable = []
    for o in headers:
        dataForTable.append(spellScroll[o])
    print(dataForTable)
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('INSERT INTO SpellsList VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', dataForTable)


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

def printSpell (spell):
    print("\n\n" + color.BOLD + color.RED + spell.name + color.END)
    print(color.UNDERLINE + "Level-" + spell.level + " " + spell.school + color.END + "\n")
    print("Casting Time: " + spell.time)
    print("Range:        " + spell.range)
    print("Components:   " + spell.comp)
    print("Duration:     " + spell.dur + "\n")
    print("Description: \n" + spell.desc)


# {'casting_time': '1 action',
#  'classes': [{'index': 'druid', 'name': 'Druid', 'url': '/api/classes/druid'},
#              {'index': 'ranger',
#               'name': 'Ranger',
#               'url': '/api/classes/ranger'}],
#  'components': ['V', 'S', 'M'],
#  'concentration': False,
#  'desc': ['Up to ten berries appear in your hand and are infused with magic '
#           'for the duration. A creature can use its action to eat one berry. '
#           'Eating a berry restores 1 hit point, and the berry provides enough '
#           'nourishment to sustain a creature for a day.',
#           'The berries lose their potency if they have not been consumed '
#           'within 24 hours of the casting of this spell.'],
#  'duration': 'Instantaneous',
#  'index': 'goodberry',
#  'level': 1,
#  'material': 'A sprig of mistletoe.',
#  'name': 'Goodberry',
#  'range': 'Touch',
#  'ritual': False,
#  'school': {'index': 'transmutation',
#             'name': 'Transmutation',
#             'url': '/api/magic-schools/transmutation'},
#  'subclasses': [],
#  'url': '/api/spells/goodberry'}