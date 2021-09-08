import Spell

spellbook = {}

def manAddSpell(book = spellbook, name):
    prompts = ["level", "dndClass", "castingTime", "spellRange", "components", "duration", "desc"]
    newSpell = {}
    for i in prompts:
        print(i + "?")
        newSpell[i] = input()
    spellbook[name] = Spell(newSpell["level"], newSpell["dndClass"], newSpell["castingTime"], newSpell["spellRange"], newSpell["components"], newSpell["duration"], newSpell["desc"])

