from tkinter import *
from tkinter.ttk import *
import saveAndLoad as sl

class slframe:
    def __init__(self, character, parent, loadFunction):
        def loadButton(event):
            value = event.widget.get()
            loadBtn = Button(self.frameUnloaded, text="Load", command=self.loadFunction(self.savedList[value]))
            loadBtn.grid(row=4, column=1, columnspan=2)

        self.frameUnloaded = Frame(parent, relief=GROOVE)
        self.frameUnloaded.columnconfigure(1, weight=1)
        self.frameUnloaded.columnconfigure(2, weight=4)
        self.frameUnloaded.rowconfigure(1, weight=1)
        self.frameUnloaded.rowconfigure(2, weight=1)
        self.frameUnloaded.rowconfigure(3, weight=1)
        self.frameUnloaded.rowconfigure(4, weight=3)

        self.frameLoaded = Frame(parent, relief=GROOVE)
            
        self.loadFunction = loadFunction

        self.parent = parent

        self.char = character

        # Create frame for load screen when no character is loaded:
        self.savedList = dict((v,k) for k,v in sl.listSavedDict().items())

        lastPlayed = Label(self.frameUnloaded, text="Last played:", font=("EB Garamond", 16))
        lastPlayedName = Label(self.frameUnloaded, text="[Name of Character]", font=("EB Garamond", 12))
        lastPlayedClass = Label(self.frameUnloaded, text="[Level-n Class]", font=("EB Garamond", 12))

        lastPlayed.grid(row=1, column=1)
        lastPlayedName.grid(row=2, column=1)
        lastPlayedClass.grid(row=3, column=1)

        unloadTitle = Label(self.frameUnloaded, text="Load a character:", font=("EB Garamond", 24))
        unloadTitle.grid(row=1, rowspan=2, column=2)
        select = Combobox(self.frameUnloaded, values=list(self.savedList.keys()), state='readonly')
        select.grid(row=3, column=2)

        select.bind('<<ComboboxSelected>>', loadButton)


    def build(self, character):
        if character != None:
            return self.frameLoaded
        else:
            return self.frameUnloaded