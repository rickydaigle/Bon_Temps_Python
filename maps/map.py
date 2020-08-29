#!/usr/bin/env python3

import random

ROOM_ID = {
    "000000":0,
    "010000":1,
    "020000":2,
    "010100":3,
    "019900":5,
    "010200":4,
    "029900":6,
    "020100":7,
    "030100":8,
    "020200":9,
    "020201":10,
    "000100":11,
    "000200":12,
    "009900":13,
    "990100":14,
    "990200":15,
    "980100":16,
    "980200":17,
    "980000":18,
    "970000":19,
    "960000":20,
    "970100":21,
    "960100":22,
    "970200":23,
    "960200":24,
    "980300":25,
    "970300":26,
    "960300":27,
    "980400":28,
    "970400":29,
    "960400":30
    
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

         {"name":"EVANGELINE THRUWAY (500 BLOCK)",
           "description":"Clean, safe, and wide, Evangeline Thruway runs north and south through the heart of Vermilionville. There are quite a few Acadian citizens walking around. Brother's shop is to the east and The Welcome Center is to the west.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n","s","e","w"]}, #01,00,00 / #1

         {"name":"BROTHER'S ON THE BOULEVARD",
           "description":"This shop sells low-level weapons and armor to the hoity-toity of River Ranch.",
           "npc":["amos","swiff"], "mob":[], "mob_chance":[], "mob_max":[], "room_level":0, "room_type":0,
           "exits":["w"]},  #02,00,00 / #2

         {"name":"EVANGELINE THRUWAY (600 BLOCK)",
           "description":"Clean, safe, and wide, Evangeline Thruway runs north and south through the heart of Vermilionville. There are a few Acadian citizens walking around. La'fayette Cemetary is to the north and Daigle Road and Gary Street branch off to the east and west respectively.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "s", "e", "w"]}, #01,01,00 / #3

         {"name":"LA'FAYETTE CEMETARY",
           "description":"At the north end of Evangeline Thruway sits the city's cemetary. It seems kind of spooky here.",
           "npc":[], "mob":[0], "mob_chance":[0.25], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["s"]}, #01,02,00 / #4

         {"name":"EVANGELINE THRUWAY (400 BLOCK)",
           "description":"Clean, safe, and wide, Evangeline Thruway runs north and south through the heart of Vermilionville. There are a few Acadian citizens walking around. The Best Stop is to the east.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "e", "w"]}, #01,99,00 / #5
         
         {"name":"THE BEST STOP",
           "description":"It smells so good in here your mouth starts to water. There are a few aisles of fresh meat and groceries, but you're instantly drawn to a display case filled with hot Cajun food.",
           "npc":["jables"], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["w"]}, #02,99,00 / #6

         {"name":"DAIGLE ROAD (100 BLOCK)",
           "description":"Daigle Road runs east from the Thruway, leading to Vermilion Swamp. There is a small, creepy house is to the north.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "e", "w"]}, #02,01,00 / #7

         {"name":"DAIGLE ROAD (200 BLOCK)",
           "description":"Daigle Road runs east from the Thruway, leading to Vermilion Swamp. Swampland stretches to the north and east as far as you can see.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["w"]}, #03,01,00 / #8

         {"name":"T'FRERE'S HOUSE",
           "description":"T'Frere the Cajun Ghost supposedly lives here.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["s", "u"]}, #02,02,00 / #9

         {"name":"T'FRERE'S ATTIC",
           "description":"A dark, spooky attic!",
           "npc":[], "mob":[1], "mob_chance":[0.10], "mob_max":[1], "room_level":5, "room_type":0,
           "exits":["d"]}, #02,02,01 / #10

         {"name":"GARY STREET (100 BLOCK)",
           "description":"Gary Street runs west from the Thruwau, leading to the Iberian cane fields. There is an advocate's office to the north.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "e", "w"]}, #00,01,00 / #11

         {"name":"THE LAW OFFICES OF MORRIS BART",
           "description":"The most famous advocate in Acadia, Morris Bart, operates from here.",
           "npc":["morris"], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["s"]}, #00,02,00 / #12

         {"name":"PREJEAN'S",
           "description":"This restaraunt attracts tourists from all over. The locals think it's OK.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #00,99,00 / #13

         {"name":"GARY STREET (200 BLOCK)",
           "description":"Gary Street runs west from the Thruwau, leading to the Iberian cane fields.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "w", "e"]}, #99,01,00 / #14

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["s", "w"]}, #99,02,00 / #15

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #98,01,00 / #16

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #98,02,00 / #17

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "w"]}, #98,00,00 / #18

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "w"]}, #97,00,00 / #19

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e"]}, #96,00,00 / #20

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #97,01,00 / #21

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s"]}, #96,01,00 / #22

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #97,02,00 / #23

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s"]}, #96,02,00 / #24

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "s", "w"]}, #98,03,00 / #25

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #97,03,00 / #26

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["n", "e", "s"]}, #96,03,00 / #27

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide. The Vermilion River is to the north, flowing peacefully.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["s", "w"]}, #98,04,00 / #28

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide. The Vermilion River is to the north, flowing peacefully.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["e", "s", "w"]}, #97,04,00 / #29

         {"name":"IBERIAN CANE FIELDS",
           "description":"The Iberian cane fields are dense mazes of cane where, according to locals, the Rougarou hide. The Vermilion River is to the north, flowing peacefully.",
           "npc":[], "mob":[2], "mob_chance":[0.2], "mob_max":[1], "room_level":3, "room_type":2,
           "exits":["e", "s"]}, #96,04,00 / #30
         ]

    # Type, Humanoid_Mobs, Animal_Mobs, Magic_Mobs
    ROOM_TYPE = [
        ["Town Inside", True, False, False],
        ["Town Outside", True, True, False],
        ["Wilderness Outside", True, True, True]
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


            
