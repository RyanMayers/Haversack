from tkinter import *
from tkinter.ttk import *
import saveAndLoad as sl
import ability as ab
import frame_ability, frame_wealth, frame_TabSaveLoad

current = None

# initialize window
root = Tk()
root.title("Haversack.py")
root.geometry('1280x720')
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

window = Frame(root)
window.grid(row=1, column=1, sticky=NSEW)


# grid bullshit
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=3)
window.columnconfigure(3, weight=1)

window.rowconfigure(1, weight=2)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=3)

# header text
header = Label(window, text="Haversack", font=("EB Garamond", 50))
header.grid(column=2, row=1)

charFrame = Frame(window)
charFrame.rowconfigure(0, weight=3)
charFrame.rowconfigure(1, weight=2)

loaded = Label(charFrame, text='(No character loaded)', font=("EB Garamond", 24))
loaded.grid(column=0, row=0)
loadedClass = Label(charFrame, text='', font=("EB Garamond", 16))
loadedClass.grid(column=0, row=1)

charFrame.grid(column=2, row=2)

# stats block
stats = frame_ability.abframe(current, window)
statsBox = stats.make()
statsBox.grid(column=1, row=3, sticky=[N,S,E])


# wealth block
wealth = frame_wealth.coinframe(current, window)
coinBox = wealth.make()
coinBox.grid(column=3, row=3, sticky=[N,S,W])

def load(index): 
    current = sl.loadChar(index)
    stats.updateBox(current)
    loaded['text'] = f"Loaded: {current.name}"
    loadedClass['text'] = f"Level-{str(current.level)} {current.gameClassName}"
    wealth.updateBox(current)

# Now for the middle section. This is all the interactible stuff.
middle = Notebook(window)

SLclass = frame_TabSaveLoad.slframe(current, middle, load)
tabSaveAndLoad = SLclass.build(current)

tabNotes = Frame(middle, relief=GROOVE)
tabSpellbook = Frame(middle, relief=GROOVE)
tabAbility = Frame(middle, relief=GROOVE)
tabInventory = Frame(middle, relief=GROOVE)
tabWealth = Frame(middle, relief=GROOVE)



middle.add(tabSaveAndLoad, text="Load/Save")
middle.add(tabNotes, text="Journal")
middle.add(tabSpellbook, text="Spellbook")
middle.add(tabAbility, text="Skills")
middle.add(tabInventory, text="Inventory")
middle.add(tabWealth, text="Coinbag")

middle.grid(column=2, row=3, padx=30, pady=30, sticky=NSEW)
window.mainloop()