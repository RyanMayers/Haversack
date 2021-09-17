import PySimpleGUI as sg                        # Part 1 - The import
import HaversackTest as h

# Define the window's contents
layout = [  [sg.Text("Import a New Spell!")],     # Part 2 - The Layout
            [sg.Text("Spell Name:        "), sg.Input(k="SName")],
            [sg.Text("Spell School:      "), sg.Input(k="School")],
            [sg.Text("Casting Class:     "), sg.Input(k="SClass")],
            [sg.Text("Spellcasting Level:"), sg.Input(k="Level")],
            [sg.Text("Casting Time:      "), sg.Input(k="CTime")],
            [sg.Text("Range:             "), sg.Input(k="SRange")],
            [sg.Text("Components:        "), sg.Checkbox("V", k="comp_v"), sg.Checkbox("S", k="comp_s"), sg.Checkbox("M", k="comp_m")],
            [sg.Text("Duration:          "), sg.Input(k="SDur")],
            [sg.Text("Description:       "), sg.Input(k="SDesc")],
            [sg.Button('Ok', bind_return_key=True)] ]

# Create the window
window = sg.Window('Add a Spell', layout)      # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

if event == "Ok":
    # self.name = name
    # self.school = school
    # self.dclass = dndClass
    # self.level = level
    # self.time = castingTime
    # self.range = spellRange
    # self.comp = components
    # self.dur = duration
    # self.desc = desc
    components = ""
    if values["comp_v"] == True:
        components.__add__("V")
    if values["comp_s"] == True:
        if not components == "":
            components.__add__(", S")
        else:
            components.__add__("S")
    if values["comp_m"] == True:
        if not components == "":
            components.__add__(", M")
        else:
            components.__add__("M")

    params = [values['SName'], values['School'], values['SClass'], values['Level'], values['CTime'], values['SRange'], components, values['SDur'], values['SDesc']]
    spellbook = {}
    h.addSpell(spellbook, params)
# Do something with the information gathered


# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window