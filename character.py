from consts import *
from ability import *

class Character:
    def __init__(self, name, stats: list, profBonus: int, profList: list, favColor):
        self.name = name
        self.color = colors[favColor]
        self.pname = f"{color.BOLD}{self.color}{self.name}{color.END}"
        self.abilities = {
            "str": stats[0],
            "dex": stats[1],
            "con": stats[2],
            "int": stats[3],
            "wis": stats[4],
            "cha": stats[5]}
        self.str = self.abilities["str"]
        self.dex = self.abilities["dex"]
        self.con = self.abilities["con"]
        self.int = self.abilities["int"]
        self.wis = self.abilities["wis"]
        self.cha = self.abilities["cha"]
        self.pb = profBonus
        self.proficiencies = profList
        self.wealth = 0 # Wealth measured in copper pieces

    def check(self, check: str, advantage = ""):
        print(getSkillCheckRoll(self, check, advantage))

    def getStats(self):
        response = f'''
{self.name}'s Ability Scores: 

Strength:     {self.str} ({abilityMod(self.str)})
Dexterity:    {self.str} ({abilityMod(self.str)})
Constitution: {self.str} ({abilityMod(self.str)})
Intelligence: {self.str} ({abilityMod(self.str)})
Wisdom:       {self.str} ({abilityMod(self.str)})
Charisma:     {self.str} ({abilityMod(self.str)})
'''
        return response