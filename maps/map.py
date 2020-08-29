#!/usr/bin/env python3

import random

ROOM_ID = {
    "000000":0,
    "010000":1,
    "020000":2,
    "010100":3,
    "019900":5,
    "010200":4,
    "029900":6
    }

def convert_xyz(x, y, z):
    if x < 0:
        x_str = str(100 + x)
    else:
        x_str = str(x)
    if y < 0:
        y_str = str(100 + y)
    else:
        y_str = str(y)
    if z < 0:
        z_str = str(100 + z)
    else:
        z_str = str(z)
    if len(x_str) < 2:
        x_str = "0" + x_str
    if len(y_str) < 2:
        y_str = "0" + y_str
    if len(z_str) < 2:
        z_str = "0" + z_str
    room_id = x_str + y_str + z_str
    return ROOM_ID[room_id]
    

class Map:

    # TBD
    ROOM = [
         {"name":"THE WELCOME CENTER",
           "description":"This large room is bright and open except for a huge pirogue statue in the middle of the room. Dozens of Acadian citizens are standing around, chatting in French. An old man approaches you and seems to want to talk.",
           "npc":["patackus"], "mob":[], "mob_chance":[], "mob_max":[], "room_level":0, "room_type":0,
           "exits":["e"]}, #00,00,00 / #0

         {"name":"CAJUN BOULEVARD (500 BLOCK)",
           "description":"Clean, safe, and wide, Cajun Boulevard runs north and south through the heart of D'aigle City. There are quite a few Acadian citizens walking around. Brother's shop is to the east and The Welcome Center is to the west.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n","s","e","w"]}, #01,00,00 / #1

         {"name":"BROTHER'S ON THE BOULEVARD",
           "description":"This shop sells low-level weapons and armor to the hoity-toity of River Ranch.",
           "npc":["amos","swiff"], "mob":[], "mob_chance":[], "mob_max":[], "room_level":0, "room_type":0,
           "exits":["w"]},  #02,00,00 / #2

         {"name":"CAJUN BOULEVARD (600 BLOCK)",
           "description":"Clean, safe, and wide, Cajun Boulevard runs north and south through the heart of D'aigle City. There are a few Acadian citizens walking around. La'fayette Cemetary is to the north.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["s", "n"]}, #01,01,00 / #3

         {"name":"LA'FAYETTE CEMETARY",
           "description":"At the north end of Cajun Boulevard sits the city's cemetary. It seems kind of spooky here.",
           "npc":[], "mob":[0], "mob_chance":[0.75], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["s"]}, #01,02,00 / #4

         {"name":"CAJUN BOULEVARD (400 BLOCK)",
           "description":"Clean, safe, and wide, Cajun Boulevard runs north and south through the heart of D'aigle City. There are a few Acadian citizens walking around. The Best Stop is to the east.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "e"]}, #01,99,00 / #5
         
         {"name":"THE BEST STOP",
           "description":"It smells so good in here your mouth starts to water. There are a few aisles of fresh meat and groceries, but you're instantly drawn to a display case filled with hot Cajun food.",
           "npc":["jables"], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["w"]}, #02,99,00 / #6
         
         ]

    # Type, Humanoid_Mobs, Animal_Mobs, Magic_Mobs
    ROOM_TYPE = [
        ["Town Inside", True, False, False],
        ["Town Outside", True, True, False]
        ]

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.id = convert_xyz(x, y, z)
        self.name = Map.ROOM[self.id]["name"]
        self.description = Map.ROOM[self.id]["description"]
        self.exits = Map.ROOM[self.id]["exits"]
        self.npc = Map.ROOM[self.id]["npc"]
        self.mob = Map.ROOM[self.id]["mob"]
        self.mob_chance = Map.ROOM[self.id]["mob_chance"]
        self.mob_max = Map.ROOM[self.id]["mob_max"]
        self.room_level = Map.ROOM[self.id]["room_level"]
        self.room_type = Map.ROOM[self.id]["room_type"]

    def print_name(self):
        return str(self.name)

    def print_description(self):
        return str(self.description)

    def return_exits(self):
        return self.exits

    def return_mobs(self):
        mob_list = []
        if self.mob:
            m = 1
            for j, each in enumerate(self.mob):
                while m <= self.mob_max[j]:
                    chance = random.random()
                    if chance <= self.mob_chance[j]:
                        mob_list.append(each)
                    m += 1
            return mob_list
        else:
            return False

    def return_npcs(self):
        npc_list = []
        if self.npc:
            npc_list = self.npc
            return npc_list
        else:
            return False


            
