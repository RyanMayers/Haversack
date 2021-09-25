class gameClass:
    def __init__(self, caster: bool, hitDie: str, savingThrows: list, proficiencies: dict):
        self.caster = caster
        self.hitDie = hitDie
        self.savingThrows = savingThrows
        self.proficiencies = proficiencies

Artificer = gameClass(
    caster=True, 
    hitDie="d8", 
    savingThrows=["con", "int"], 
    proficiencies={
        "Armor":["Light armor, medium armor, shields"],
        "Weapons":["Simple weapons"],
        "Tools":["Thieves’ tools, tinker’s tools, one type of artisan’s tools of your choice"]
    }
)

Barbarian = gameClass(
    caster=False, 
    hitDie="d12", 
    savingThrows=["str", "con"], 
    proficiencies={
        "Armor":["Light armor, medium armor, shields"],
        "Weapons":["Simple weapons, martial weapons"],
        "Tools":["None"]
    }
)

Bard = gameClass(
    caster=True, 
    hitDie="d8", 
    savingThrows=["dex", "cha"], 
    proficiencies={
        "Armor":["Light armor"],
        "Weapons":["Simple weapons, hand crossbows, longswords, rapiers, shortswords"],
        "Tools":["Three musical instruments of your choice"]
    }
)

Cleric = gameClass(
    caster=True, 
    hitDie="d8", 
    savingThrows=["wis", "cha"], 
    proficiencies={
        "Armor":["Light armor, medium armor, shields"],
        "Weapons":["All simple weapons"],
        "Tools":["None"]
    }
)

Druid = gameClass(
    caster=True, 
    hitDie="d8", 
    savingThrows=["int", "wis"], 
    proficiencies={
        "Armor":["Light armor, medium armor, shields (druids will not wear armor or use shields made of metal)"],
        "Weapons":["Clubs, daggers, darts, javelins, maces, quarterstaffs, scimitars, sickles, slings, spears"],
        "Tools":["Herbalism kit"]
    }
)

Fighter = gameClass(
    caster=False, 
    hitDie="d10", 
    savingThrows=["str", "con"], 
    proficiencies={
        "Armor":["All armor, shields"],
        "Weapons":["Simple weapons, martial weapons"],
        "Tools":["None"]
    }
)

Monk = gameClass(
    caster=True, 
    hitDie="d8", 
    savingThrows=["str", "dex"], 
    proficiencies={
        "Armor":["None"],
        "Weapons":["Simple weapons, shortswords"],
        "Tools":["Choose one type of artisan's tools or one musical instrument."]
    }
)

Paladin = gameClass(
    caster=True, 
    hitDie="d10", 
    savingThrows=["wis", "cha"], 
    proficiencies={
        "Armor":["All armor, shields"],
        "Weapons":["Simple weapons, martial weapons"],
        "Tools":["None"]
    }
)

Ranger = gameClass(
    caster=True, 
    hitDie="d10", 
    savingThrows=["str", "dex"], 
    proficiencies={
        "Armor":["Light armor, medium armor, shields"],
        "Weapons":["Simple weapons, martial weapons"],
        "Tools":["None"]
    }
)

Rogue = gameClass(
    caster=False, 
    hitDie="d8", 
    savingThrows=["dex", "int"], 
    proficiencies={
        "Armor":["Light armor"],
        "Weapons":["Simple weapons, hand crossbows, longswords, rapiers, shortswords"],
        "Tools":["Thieves' tool"]
    }
)

Sorcerer = gameClass(
    caster=True, 
    hitDie="d6", 
    savingThrows=["con", "cha"], 
    proficiencies={
        "Armor":["None"],
        "Weapons":["Daggers, darts, slings, quarterstaffs, light crossbows"],
        "Tools":["None"]
    }
)

Warlock = gameClass(
    caster=True, 
    hitDie="d8", 
    savingThrows=["wis", "cha"], 
    proficiencies={
        "Armor":["Light armor"],
        "Weapons":["Simple weapons"],
        "Tools":["None"]
    }
)

Wizard = gameClass(
    caster=True, 
    hitDie="d6", 
    savingThrows=["int", "wis"], 
    proficiencies={
        "Armor":["None"],
        "Weapons":["Daggers, darts, slings, quarterstaffs, light crossbows"],
        "Tools":["None"]
    }
)

classlist = {
    'Artificer': Artificer,
    'Barbarian': Barbarian,
    'Bard': Bard,
    'Cleric': Cleric,
    'Druid': Druid,
    'Fighter': Fighter,
    'Monk': Monk,
    'Paladin': Paladin,
    'Ranger': Ranger,
    'Rogue': Rogue,
    'Sorcerer': Sorcerer,
    'Warlock': Warlock,
    'Wizard': Wizard
}