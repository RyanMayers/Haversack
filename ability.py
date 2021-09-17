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
        print(f"\n\n{self.pname} Skill Check: {color.BOLD}{check}{color.END}")
        for i in categories:
            if check in categories[i]:
                mod = abilityMod(self.abilities[i])
        if check in self.proficiencies:
            mod += self.pb
        return rolldice.roll_dice(f'{num}d20{adv} + {mod}')
    
    # Ability Check
    elif check in abilities:
        print(f"\n\n{self.pname} Ability Check: {color.BOLD}{ablLong[check]}{color.END}")
        mod = abilityMod(self.abilities[check])
        return rolldice.roll_dice(f'{num}d20{adv} + {mod}')
    
    # Unrecognized Input
    else:
        print(f"{check} is not a valid skill or ability.")