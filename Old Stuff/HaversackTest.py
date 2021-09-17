from Spell import *

spellbook = {}

def manAddSpell(book):
    prompts = ["name", "school", "level", "dndClass", "castingTime", "spellRange", "components", "duration", "desc"]
    newSpell = {}
    for i in prompts:
        print(i + "?")
        newSpell[i] = input()
    book[newSpell["name"]] = Spell(newSpell["name"], newSpell["school"], newSpell["level"], newSpell["dndClass"], newSpell["castingTime"], newSpell["spellRange"], newSpell["components"], newSpell["duration"], newSpell["desc"])

def addSpell(book, params):
    prompts = ["name", "school", "level", "dndClass", "castingTime", "spellRange", "components", "duration", "desc"]
    newSpell = {}
    j = 0
    for i in prompts:
        newSpell[i] = params[j]
        j += 1
    book[newSpell["name"]] = Spell(newSpell["name"], newSpell["school"], newSpell["level"], newSpell["dndClass"], newSpell["castingTime"], newSpell["spellRange"], newSpell["components"], newSpell["duration"], newSpell["desc"])

    print("Spell Added:\n")
    printSpell(book["name"])

def addSpellAPI(book, name):
    data = getSpell(name)
    

        # self.name = name
        # self.school = school
        # self.dclass = dndClass
        # self.level = level
        # self.time = castingTime
        # self.range = spellRange
        # self.comp = components
        # self.dur = duration
        # self.desc = desc

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
