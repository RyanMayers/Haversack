from tkinter import Frame, Grid, Label, GROOVE
from countables import coinbag as cb

class coinframe:
    def __init__(self, character, parent):
        self.frame = Frame(parent, borderwidth=5, relief=GROOVE)

        self.frame.columnconfigure(0, weight=3)
        self.frame.columnconfigure(1, weight=3)
        self.frame.columnconfigure(2, weight=2)
        self.frame.rowconfigure(0, weight=1, pad=3)
        self.frame.rowconfigure(1, weight=1, pad=3)
        self.frame.rowconfigure(2, weight=1, pad=3)
        self.frame.rowconfigure(3, weight=1, pad=3)
        self.frame.rowconfigure(4, weight=1, pad=3)

        self.character = character

        self.array = {
            "cp": 1000,
            "sp": 100,
            "ep": 50,
            "gp": 10,
            "pp": 1}

        if character != None:
            self.array = cb.sortCoins(Copper=character.rawWealth)
        
        # Column 1: Coin Denominations
        self.cpLabel = Label(self.frame, text="CP:", font=("EB Garamond", 18), bd=2)
        self.spLabel = Label(self.frame, text="SP:", font=("EB Garamond", 18), bd=2)
        self.epLabel = Label(self.frame, text="EP:", font=("EB Garamond", 18), bd=2)
        self.gpLabel = Label(self.frame, text="GP:", font=("EB Garamond", 18), bd=2)
        self.ppLabel = Label(self.frame, text="PP:", font=("EB Garamond", 18), bd=2)

        self.cpLabel.grid(column=0, row=0)
        self.spLabel.grid(column=0, row=1)
        self.epLabel.grid(column=0, row=2)
        self.gpLabel.grid(column=0, row=3)
        self.ppLabel.grid(column=0, row=4)
        

        # Column 2: Coin Values
        self.cpLabel = Label(self.frame, text=str(self.array["cp"]), font=("EB Garamond", 24), bd=2)
        self.spLabel = Label(self.frame, text=str(self.array["sp"]), font=("EB Garamond", 24), bd=2)
        self.epLabel = Label(self.frame, text=str(self.array["ep"]), font=("EB Garamond", 24), bd=2)
        self.gpLabel = Label(self.frame, text=str(self.array["gp"]), font=("EB Garamond", 24), bd=2)
        self.ppLabel = Label(self.frame, text=str(self.array["pp"]), font=("EB Garamond", 24), bd=2)

        self.cpLabel.grid(column=1, row=0)
        self.spLabel.grid(column=1, row=1)
        self.epLabel.grid(column=1, row=2)
        self.gpLabel.grid(column=1, row=3)
        self.ppLabel.grid(column=1, row=4)

    def updateBox(self, character):
        if character != None:
            self.array = cb.sortCoins(Copper=character.rawWealth)

        self.character = character

        self.cpLabel['text'] = str(self.array["cp"])
        self.spLabel['text'] = str(self.array["sp"])
        self.epLabel['text'] = str(self.array["ep"])
        self.gpLabel['text'] = str(self.array["gp"])
        self.ppLabel['text'] = str(self.array["pp"])
    
    def make(self):
        return self.frame