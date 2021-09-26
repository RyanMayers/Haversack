from tkinter import *
from tkinter.ttk import *
from ability import abilityMod as abm

class abframe:
    def __init__(self, character, parent):
        self.frame = Frame(parent, borderwidth=5, relief=GROOVE, padding=30)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1, pad=3)
        self.frame.rowconfigure(1, weight=1, pad=3)
        self.frame.rowconfigure(2, weight=1, pad=3)
        self.frame.rowconfigure(3, weight=1, pad=3)
        self.frame.rowconfigure(4, weight=1, pad=3)
        self.frame.rowconfigure(5, weight=1, pad=3)

        self.character = character

        self.array = {
            "str": 10,
            "dex": 10,
            "con": 10,
            "int": 10,
            "wis": 10,
            "cha": 10}
        if character != None:
            for i in character.stats:
                self.array[i] = int(character.stats[i])
        
        # Column 1: Ability Score Labels
        self.StrLabel = Label(self.frame, text="STR:", font=("EB Garamond", 18), padding=2)
        self.DexLabel = Label(self.frame, text="DEX:", font=("EB Garamond", 18), padding=2)
        self.ConLabel = Label(self.frame, text="CON:", font=("EB Garamond", 18), padding=2)
        self.IntLabel = Label(self.frame, text="INT:", font=("EB Garamond", 18), padding=2)
        self.WisLabel = Label(self.frame, text="WIS:", font=("EB Garamond", 18), padding=2)
        self.ChaLabel = Label(self.frame, text="CHA:", font=("EB Garamond", 18), padding=2)

        self.StrLabel.grid(column=0, row=0)
        self.DexLabel.grid(column=0, row=1)
        self.ConLabel.grid(column=0, row=2)
        self.IntLabel.grid(column=0, row=3)
        self.WisLabel.grid(column=0, row=4)
        self.ChaLabel.grid(column=0, row=5)
        

        # Column 2: Ability Score Modifiers
        self.StrModLabel = Label(self.frame, text=str(abm(self.array["str"])), font=("EB Garamond", 24), padding=2)
        self.DexModLabel = Label(self.frame, text=str(abm(self.array["dex"])), font=("EB Garamond", 24), padding=2)
        self.ConModLabel = Label(self.frame, text=str(abm(self.array["con"])), font=("EB Garamond", 24), padding=2)
        self.IntModLabel = Label(self.frame, text=str(abm(self.array["int"])), font=("EB Garamond", 24), padding=2)
        self.WisModLabel = Label(self.frame, text=str(abm(self.array["wis"])), font=("EB Garamond", 24), padding=2)
        self.ChaModLabel = Label(self.frame, text=str(abm(self.array["cha"])), font=("EB Garamond", 24), padding=2)
        self.StrModLabel.grid(column=1, row=0)
        self.DexModLabel.grid(column=1, row=1)
        self.ConModLabel.grid(column=1, row=2)
        self.IntModLabel.grid(column=1, row=3)
        self.WisModLabel.grid(column=1, row=4)
        self.ChaModLabel.grid(column=1, row=5)


        # Column 3: Raw Ability Scores

        self.StrStatLabel = Label(self.frame, text=f'({str(self.array["str"])})', font=("EB Garamond", 12), padding=2)
        self.DexStatLabel = Label(self.frame, text=f'({str(self.array["dex"])})', font=("EB Garamond", 12), padding=2)
        self.ConStatLabel = Label(self.frame, text=f'({str(self.array["con"])})', font=("EB Garamond", 12), padding=2)
        self.IntStatLabel = Label(self.frame, text=f'({str(self.array["int"])})', font=("EB Garamond", 12), padding=2)
        self.WisStatLabel = Label(self.frame, text=f'({str(self.array["wis"])})', font=("EB Garamond", 12), padding=2)
        self.ChaStatLabel = Label(self.frame, text=f'({str(self.array["cha"])})', font=("EB Garamond", 12), padding=2)
        self.StrStatLabel.grid(column=2, row=0)
        self.DexStatLabel.grid(column=2, row=1)
        self.ConStatLabel.grid(column=2, row=2)
        self.IntStatLabel.grid(column=2, row=3)
        self.WisStatLabel.grid(column=2, row=4)
        self.ChaStatLabel.grid(column=2, row=5)

    def updateBox(self, character):
        if character != None:
            for i in character.stats:
                self.array[i] = int(character.stats[i])

        self.character = character

        self.StrModLabel['text'] = str(abm(self.array["str"]))
        self.DexModLabel['text'] = str(abm(self.array["dex"]))
        self.ConModLabel['text'] = str(abm(self.array["con"]))
        self.IntModLabel['text'] = str(abm(self.array["int"]))
        self.WisModLabel['text'] = str(abm(self.array["wis"]))
        self.ChaModLabel['text'] = str(abm(self.array["cha"]))

        self.StrStatLabel['text'] = f'({str(self.array["str"])})'
        self.DexStatLabel['text'] = f'({str(self.array["dex"])})'
        self.ConStatLabel['text'] = f'({str(self.array["con"])})'
        self.IntStatLabel['text'] = f'({str(self.array["int"])})'
        self.WisStatLabel['text'] = f'({str(self.array["wis"])})'
        self.ChaStatLabel['text'] = f'({str(self.array["cha"])})'
    
    def make(self):
        return self.frame