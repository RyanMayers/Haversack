from character import Character

class Fighter(Character):
    def __init__(self, level, abilities):
        super().__init__(self, name="", gameclass="", stats=abilities, profList:list, level = level, favColor = "GREEN", wealth = 0)