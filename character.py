import consts
from consts import color
from consts import text
import ability
import coinbag
import gameClasses

class Character:
    def __init__(self, name, gameclass, stats: list, profList: list, level = 1, favColor = "GREEN", wealth = 0):
        self.name = name
        self.gameClass = gameClasses.gameClasses[gameclass]
        self.level = level
        self.favColor = favColor
        self.color = consts.colors[favColor]
        self.pname = f"{consts.color.BOLD}{self.color}{self.name}{consts.color.END}"
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
        self.hitDice = str(self.level) + self.gameClass.hitDie
        self.pb = consts.profBonus[level]
        self.proficiencies = profList
        self.rawWealth = wealth # Wealth measured in copper pieces

    def check(self, check: str, advantage = ""):
        ability.getSkillCheckRoll(self, check, advantage)

    def levelUp(self, newLevel: int):
        # This function is gonna need a whole bunch more stuff as this program gets more elaborate
        try:
            if newLevel <= self.level:
                raise consts.LevelBelowCurrent
            oldLevel = self.level
            self.level = newLevel
            oldPB = self.pb
            self.pb = consts.profBonus[self.level]
            oldHitDice = self.hitDice
            self.hitDice = str(self.level) + self.gameClass.hitDie
            print(f"\n{self.pname} leveled up! Here's what changed:\n")
            print(f"Level:              {oldLevel}   -> {color.BOLD}{color.GREEN2}{newLevel}{color.END}")
            if self.pb != oldPB:
                print(f"Proficiency Bonus:  {oldPB}   -> {color.BOLD}{color.GREEN2}{self.pb}{color.END}")
            print(f"Hit Dice:           {oldHitDice} -> {color.BOLD}{color.GREEN2}{self.hitDice}{color.END}")
            print("\n")
        except consts.LevelBelowCurrent:
            print("You can't level up a character below your current level! Please enter the NEW character level with this function.")

    def addWealth(self, Copper = 0, Silver = 0, Electrum = 0, Gold = 0, Platinum = 0):
        coins = [Copper, Silver, Electrum, Gold, Platinum]
        coinText = [text.CP, text.SP, text.EP, text.GP, text.PP]
        numTypes = 0
        multi = False
        for i in coins:
            if i != 0:
                numTypes += 1
        if numTypes > 1:
            multi = True
        response = "\nAdded "
        iters = 0
        for j in coins:
            if j != 0:
                if numTypes == 1 and multi:
                    response += "and "
                response += f"{j} {coinText[iters]}"
                if numTypes > 1:
                    response += ","
                response += " "
                numTypes -= 1
            iters += 1
        response += f"to {self.pname}'s coinbag."
        print(response)
        self.rawWealth += coinbag.rawWealth(Copper, Silver, Electrum, Gold, Platinum)

    def wealth(self):
        coins = coinbag.sortCoins(self.rawWealth)
        response = f'''
{self.pname}'s Wealth: 

{color.BOLD}{coins['pp']}{color.END} {text.PLATINUM}
{color.BOLD}{coins['gp']}{color.END} {text.GOLD}
{color.BOLD}{coins['ep']}{color.END} {text.ELECTRUM}
{color.BOLD}{coins['sp']}{color.END} {text.SILVER}
{color.BOLD}{coins['cp']}{color.END} {text.COPPER}  
        '''
        return response

    def getStats(self):
        response = f'''
{self.pname}'s Ability Scores: 

Strength:     {self.str} ({ability.abilityMod(self.str)})
Dexterity:    {self.dex} ({ability.abilityMod(self.dex)})
Constitution: {self.con} ({ability.abilityMod(self.con)})
Intelligence: {self.int} ({ability.abilityMod(self.int)})
Wisdom:       {self.wis} ({ability.abilityMod(self.wis)})
Charisma:     {self.cha} ({ability.abilityMod(self.cha)})
'''
        return response