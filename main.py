from tkinter import *
from tkinter import ttk

# programming sucks i hate this why do i have to do all the thinking for the computer it's supposed to do it for me what the fuck

root = Tk()
root.geometry("100x100")
root.title("peepee poopoo")

frame = Frame(root)
frame.pack()

button = Button(root, text="press this and i die instantly",
                command = root.destroy)

button.pack(side='top')

root.mainloop()