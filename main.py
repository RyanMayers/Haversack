import Spell
import requests, json
import rolldice as d
import ability
import character
import consts
import saveAndLoad as sl
import os

def clear():
    os.system('clear')

clear()
print(f'''
{consts.color.BOLD}Welcome to Haversack!{consts.color.END}









Type "load" to load a character, or "help" to see what else you can do!"

What would you like to do?
''')

i = input(">")

if i == "load":
    load()
elif i == "help":
    print("I haven't written the help section yet.")
elif i == "quit":
    quit()

def load():

    clear()
    print(f'''
{consts.color.BOLD}HAVERSACK{consts.color.END}



Which saved character would you like to load?

''')
    sl.listSaved()
    print("\n")
    j = int(input(">"))-1
    try:
        current = sl.loadChar(str(j))
    except:
        print("Error loading character!")

print(f'''
{consts.color.BOLD}Welcome to Haversack!{consts.color.END}

What would you like to do?
''')

p = input(">")

if p == "Check":
    print("")