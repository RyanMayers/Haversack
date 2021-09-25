from tkinter import *
import saveAndLoad as sl
import ability as ab
import frame_ability, frame_wealth

current = None

# temporary, just immediately loads first saved character.


# initialize window
window = Tk()
window.title("Haversack.py")
window.geometry('600x400')


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

charFrame = Frame(window, bd=5)
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
statsBox.grid(column=1, row=3)


# wealth block
wealth = frame_wealth.coinframe(current, window)
coinBox = wealth.make()
coinBox.grid(column=3, row=3)

def load(): 
    current = sl.loadChar(0)
    stats.updateBox(current)
    loaded['text'] = f"Loaded: {current.name}"
    loadedClass['text'] = f"Level-{str(current.level)} {current.gameClassName}"
    wealth.updateBox(current)

loadBtn = Button(window, text="Load Character", command=load)
loadBtn.grid(column=2, row=3)

window.mainloop()