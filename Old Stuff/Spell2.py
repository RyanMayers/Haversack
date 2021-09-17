import requests
import pprint
import json
import sqlite3

class Spell:
    "A spell is a magical effect that a caster can unleash through their knowledge, skill, or training. Magical energy interweaves and permeates the universe, and casters can manipulate this to their benefit."
    def __init__(self, index):
        info = getJsonSpell(index)
        self.index = index
        self.name = info["name"]

def initTable(dbName):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    sql = f'''CREATE TABLE {dbName}(
    ID TEXT PRIMARY KEY,
    NAME TEXT,
    LEVEL INTEGER,
    SCHOOL TEXT,
    JSON TEXT NOT NULL
    )
    '''
    cur.execute(sql)
    conn.commit()
    conn.close()

def cleanName(inputName):
    return inputName.replace(' ', '-').lower()

def spellAPI(name):
    spell = cleanName(name)
    url = "https://www.dnd5eapi.co/api/spells/"
    return requests.request("GET", url + spell)

def addToDB(spell, table):
    try:
        data = spellAPI(spell).json()
        # data = json.loads(dataJSON)
        dbindex = data["index"]
        name = data["name"]
        level = data["level"]
        school = data["school"]["index"]
        conn = sqlite3.connect('database.db')
        dataSTR = json.dumps(data, indent = 4)
        cur = conn.cursor()
        sql = f"INSERT INTO {table} VALUES ('{dbindex}', '{name}', {level}, '{school}', {dataSTR})"
        print(sql)
        cur.execute(sql)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
    conn.close()

def getJsonSpell(dbindex):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    sql = f'''SELECT * FROM SPELLS_MASTER WHERE ID = {dbindex}'''
    cur.execute(sql)
    row = cur.fetchone()
    return json.loads(row)

# def printSpell (spell):
#     print("\n\n" + color.BOLD + color.RED + spell.name + color.END)
#     print(color.UNDERLINE + inflect(spell.level) + ]"Level" + " " + spell.school + color.END + "\n")
#     print("Casting Time: " + spell.time)
#     print("Range:        " + spell.range)
#     print("Components:   " + spell.comp)
#     print("Duration:     " + spell.dur + "\n")
#     print("Description: \n" + spell.desc)