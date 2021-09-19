import math
import rolldice
from consts import *

def abilityMod(score):
    return math.floor((score-10)/2)

def getSkillCheckRoll(self, check, advantage):
    # Handle Advantage
    if advantage in ["adv", "advantage", "a"]:
        adv = "K"
        num = 2
    elif advantage in ["dis", "disadvantage", "d"]:
        adv = "k"
        num = 2
    else:
        adv = ""
        num = 1

    # Skill Check
    if check in skills:
        # Header Print for Skill Check
        for i in categories:
            if check in categories[i]:
                mod = abilityMod(self.abilities[i])
        if check in self.proficiencies:
            mod += self.pb
        modStr = f"{str(mod)}"
        if mod >= 0:
            modStr = f"+{str(mod)}"
        print(f"\n\n{self.pname} Skill Check: {color.BOLD}{check}{color.END} ({modStr})")
        roll = rolldice.roll_dice(f'{num}d20{adv} + {mod}')
        print(bigNums[roll[0]])
    
    # Ability Check
    elif check in abilities:
        mod = abilityMod(self.abilities[check])
        modStr = f"{str(mod)}"
        if mod >= 0:
            modStr = f"+{str(mod)}"
        print(f"\n\n{self.pname} Ability Check: {color.BOLD}{ablLong[check]}{color.END} ({modStr})")
        roll = rolldice.roll_dice(f'{num}d20{adv} + {mod}')
        print(bigNums[roll[0]])
    
    # Unrecognized Input
    else:
        print(f"{check} is not a valid skill or ability.")