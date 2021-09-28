from tkinter import *
from tkinter.ttk import *
from json import load
import Spell as s

class spellFrame:
    def __init__(self, character, parent):
        # Initialize the master frame for this tab. This contains two frames: the Selection Frame, for choosing which spell to get the info for, and the Info Frame, for displaying the info on that spell.

        self.frame = Frame(parent, borderwidth=5, relief=GROOVE, padding=30)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=2)
        self.frame.rowconfigure(1, weight=1)

        # Just keeping these variables somewhere in case I need them. Parent is only really needed for the master frame, but Character will be useful when character-dependent spellbooks are implemented. For now, though, all spells are displayable.
        self.character = character
        self.parent = parent

        # Get the full list of available spells to display.
        with open("./gather spells/SpellCatalog.json") as file:
            catalog = list(load(file)["SpellList"])
            file.close()

        self.catalog = catalog
        self.indices = {}

        # Part 1: the Selection Frame. I considered using pack() here but it seems that mixing that and grid() is a no no.
        selectFrame = Frame(self.frame)
        selectFrame.columnconfigure(1, weight=1)
        selectFrame.rowconfigure(1, weight=10)
        selectFrame.rowconfigure(2, weight=1)
        selectFrame.rowconfigure(3, weight=1)
        selectFrame.grid(row=1, column=0, sticky=NSEW)
        
        # Initialize the list of selectable spells and add the full catalog. There might be a more elegant way to do this than iterating but it works.
        chooseSpell = Listbox(selectFrame)
        iters = 0
        for i in catalog:
            chooseSpell.insert(iters, i)
            self.indices[i] = iters
            iters += 1

        # Function to update description box with info when a spell is selected.        
        def spellSelect(event):
            infoBox['state']=NORMAL
            infoBox.delete("1.0", END)
            w = event.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            selection['text'] = value
            infoBox.insert(END, s.spellInfo(value))
            infoBox['state']=DISABLED


        # Bind the selection list to update the info box.
        chooseSpell.bind('<<ListboxSelect>>', spellSelect)

        # Place the selection list.
        chooseSpell.grid(row=1, column=1, sticky=NS)

        # Add an entry box for searching manually..
        searchBox = Entry(selectFrame)
        searchBox.grid(row=2, column=1)

        # ...a function that sanitizes the input, sets the listbox to the correct spell, and updates the reference box...
        def spellSearch(event=None):
            term = searchBox.get()
            infoBox['state']=NORMAL
            infoBox.delete("1.0", END)
            value = s.sani(term)
            infoBox.insert(END, s.spellInfo(value))
            fullName = s.spellLookup(value)["name"]
            index = self.indices[fullName]
            selection['text'] = fullName
            chooseSpell.selection_set(index)
            infoBox['state']=DISABLED

        searchBox.bind('<Return>', spellSearch)

        # ...and a button to send the search.
        searchBtn = Button(selectFrame, command=spellSearch, text="Search")
        searchBtn.grid(row=3, column=1)

        # Part 2: the Info Frame. First, initialize it.
        self.infoFrame = Frame(self.frame, padding=10)

        self.infoFrame.columnconfigure(1, weight=1)
        self.infoFrame.rowconfigure(1, weight=1)
        self.infoFrame.rowconfigure(2, weight=2)
        
        selection = Label(self.infoFrame, font=("EB Garamond", 24), text="")
        selection.grid(row=1, column=1)

        infoBox = Text(self.infoFrame, bg="light yellow", font=("Courier", 16), width=40, height=15, wrap=WORD)
        infoBox.grid(row=2, column=1, sticky=NSEW)

        self.infoFrame.grid(row=1, column=1, sticky=NSEW)