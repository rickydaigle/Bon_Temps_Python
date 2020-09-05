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
    "960400":30,
    "030200":31,
    "030300":32,
    "030400":33,
    "040200":34,
    "040300":35,
    "040400":36,
    "040100":37,
    "040000":38,
    "050200":39,
    "050300":40,
    "050400":41,
    "050100":42,
    "050000":43,
    "019800":44,
    "019700":45,
    "019600":46,
    "009600":47,
    "019500":48,
    "009500":49,
    "999500":50,
    "989500":51,
    "029500":52,
    "039500":53,
    "049500":54,
    "059500":55,
    "069500":56,
    "079500":57,
    "049400":58,
    "049300":59,
    "049200":60,
    "039300":61,
    "029100":62,
    "039100":63,
    "049100":64,
    "059100":65,
    "069100":66,
    "029000":67,
    "039000":68,
    "049000":69,
    "059000":70,
    "069000":71,
    "028900":72,
    "038900":73,
    "048900":74,
    "058900":75,
    "068900":76,
    "079600":77,
    "079700":78,
    "079400":79,
    "029800":80,
    "079300":81,
    "069400":82,
    "089400":83,
    "069600":84,
    "089600":85,
    "069700":86,
    "089700":87,
    "069800":88,
    "079800":89,
    "089800":90,
    "069900":91,
    "079900":92,
    "089900":93,
    "060000":94,
    "070000":95,
    "080000":96,
    "009800":97,
    "999800":98,
    "989800":99,
    "010300":100
    
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
         {"name":"THE CAJUN HEARTLAND WELCOME CENTER",
           "description":"This large room is bright and open except for a huge pirogue statue in the middle of the room. Dozens of Acadian citizens are standing around, chatting in French. An old man approaches you and seems to want to talk. You should probably type his name to see what he wants.",
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
           "description":"At the north end of Evangeline Thruway sits the city's cemetary. It seems kind of spooky here. A beautiful cathedral is north of here.",
           "npc":[], "mob":[0], "mob_chance":[0.25], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["n", "s"]}, #01,02,00 / #4

         {"name":"EVANGELINE THRUWAY (400 BLOCK)",
           "description":"Clean, safe, and wide, Evangeline Thruway runs north and south through the heart of Vermilionville. There are a few Acadian citizens walking around. The Best Stop is to the east.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "e", "s", "w"]}, #01,99,00 / #5
         
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
           "exits":["n", "e", "w"]}, #03,01,00 / #8

         {"name":"T'FRERE'S HOUSE",
           "description":"T'Frere the Cajun Ghost supposedly lives here.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["s", "u"]}, #02,02,00 / #9

         {"name":"T'FRERE'S ATTIC",
           "description":"A dark, spooky attic!",
           "npc":[], "mob":[1], "mob_chance":[0.10], "mob_max":[1], "room_level":5, "room_type":0,
           "exits":["d"]}, #02,02,01 / #10

         {"name":"GARY STREET (100 BLOCK)",
           "description":"Gary Street runs west from the Thruway, leading to the Iberian cane fields. There is an advocate's office to the north.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "e", "w"]}, #00,01,00 / #11

         {"name":"THE LAW OFFICES OF MORRIS BART",
           "description":"The most famous advocate in Acadia, Morris Bart, operates from here. The Vermilionville Sheriff and his deputies also operate out of this building.",
           "npc":["morris"], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["s"]}, #00,02,00 / #12

         {"name":"PREJEAN'S",
           "description":"This restaraunt attracts tourists from all over. The locals think it's OK.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #00,99,00 / #13

         {"name":"GARY STREET (200 BLOCK)",
           "description":"Gary Street runs west from the Thruway, leading to the Iberian cane fields.",
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

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "e", "s"]}, #03,02,00 / #31

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "e", "s"]}, #03,03,00 / #32

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!. The Vermilion River is to the north, flowing peacefully.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["e", "s"]}, #03,04,00 / #33

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #04,02,00 / #34

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #04,03,00 / #35

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!. The Vermilion River is to the north, flowing peacefully.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["e", "s", "w"]}, #04,04,00 / #36

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "e", "s", "w"]}, #04,01,00 / #37

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "e"]}, #04,00,00 / #38

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!. The mighty Miss Sippy River is to the east.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "s", "w"]}, #05,02,00 / #39

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!. The mighty Miss Sippy River is to the east.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "s", "w"]}, #05,03,00 / #40

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!. The Vermilion River is to the north, and the mighty Miss Sippy River is to the east.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["s", "w"]}, #05,04,00 / #41

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!. The mighty Miss Sippy River is to the east.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "s", "w"]}, #05,01,00 / #42

         {"name":"VERMILLION SWAMP",
           "description":"The Vermilionville swamp is full of dangerous wildlife, some that taste really good when cooked with a roux!. To the east the swamp dries up into a forest.",
           "npc":[], "mob":[5], "mob_chance":[0.12], "mob_max":[2], "room_level":2, "room_type":2,
           "exits":["n", "e", "w"]}, #05,00,00 / #43

         {"name":"EVANGELINE THRUWAY (300 BLOCK)",
           "description":"Clean, safe, and wide, Evangeline Thruway runs north and south through the heart of Vermilionville. There are quite a few Acadian citizens walking around. Evangeline Downs is to the east.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n","s","e"]}, #01,98,00 / #44

         {"name":"EVANGELINE THRUWAY (200 BLOCK)",
           "description":"Clean, safe, and wide, Evangeline Thruway runs north and south through the heart of Vermilionville. There are a few Acadian citizens walking around.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n","s"]}, #01,97,00 / #45

         {"name":"EVANGELINE THRUWAY (100 BLOCK)",
           "description":"Clean, safe, and wide, Evangeline Thruway runs north and south through the heart of Vermilionville. The Troop I Highwayman barracks is to the west.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n","s", "w"]}, #01,96,00 / #46

         {"name":"ACADIA HIGHWAYMEN TROOP I",
           "description":"The Vermilionville HQ of the kingdom's highwaymen: troopers who keep the roads free of land pirates.",
           "npc":[5], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #00,96,00 / #47

         {"name":"I-10 MILE 103",
           "description":"The Vermilionville Exit of the Acadia Interkingdom Highway. I-10 runs east & west. You see a bunch of drilling rigs in the distance to the south but you don't see how to get there.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n"]}, #01,95,00 / #48

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #00,95,00 / #49

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #99,95,00 / #50

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e"]}, #98,95,00 / #51

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #02,95,00 / #52

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #03,95,00 / #53

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas. Couyon Road runs to the south.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #04,95,00 / #54

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #05,95,00 / #55

         {"name":"INTERKINGDOM 10 HIGHWAY",
           "description":"The Acadia Interkingdom Highway runs east & west, connecting Vermilionville to Red City and other areas.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #06,95,00 / #56

         {"name":"I-10 MILE 155",
           "description":"The Red City Exit of the Acadia Interkingdom Highway. The Aerodrome Highway runs north and south through the Capital of Acadia.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "w"]}, #07,95,00 / #57

         {"name":"COUYON ROAD (100 BLOCK)",
           "description":"Couyon Road runs north to I-10 and south to the Atchafalaya Swamp.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "s"]}, #04,94,00 / #58

         {"name":"COUYON ROAD (200 BLOCK)",
           "description":"Couyon Road runs north to I-10 and south to the Atchafalaya Swamp. There is a Highwaymen post to the west.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "s", "w"]}, #04,93,00 / #59

         {"name":"COUYON ROAD (300 BLOCK)",
           "description":"Couyon Road runs north to I-10 and south to the Atchafalaya Swamp.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "s"]}, #04,92,00 / #60

         {"name":"ACADIA HIGHWAYMEN ATCHAFALAYA POST",
           "description":"The building itself looks run down, but the highwaymen milling around still keep clean-shaven faces and wear shiny armor.",
           "npc":[7], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #03,93,00 / #61

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["s", "e"]}, #02,91,00 / #62

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["s", "e", "w"]}, #03,91,00 / #63

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "s", "e", "w"]}, #04,91,00 / #64

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["s", "e", "w"]}, #05,91,00 / #65

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["s", "w"]}, #06,91,00 / #66

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "s", "e"]}, #02,90,00 / #67

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "s", "e", "w"]}, #03,90,00 / #68

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "s", "e", "w"]}, #04,90,00 / #69

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "s", "e", "w"]}, #05,90,00 / #70

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "s", "w"]}, #06,90,00 / #71

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead. The Gulf of Canadia is to the south.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "e"]}, #02,89,00 / #72

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead. The Gulf of Canadia is to the south.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "e", "w"]}, #03,89,00 / #73

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead. The Gulf of Canadia is to the south.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "e", "w"]}, #04,89,00 / #74

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead. The Gulf of Canadia is to the south.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "e", "w"]}, #05,89,00 / #75

         {"name":"ATCHAFALAYA SWAMP",
           "description":"The Atchafalaya Swamp is picturesque, but full of critters that want you dead. The Gulf of Canadia is to the south.",
           "npc":[], "mob":[4], "mob_chance":[.1], "mob_max":[1], "room_level":4, "room_type":1,
           "exits":["n", "w"]}, #06,89,00 / #76

         {"name":"AERODROME HIGHWAY NORTH (100 BLOCK)",
           "description":"Aerodrome Highway is a large, busy road running north and south through Red City, the Capital of Acadia.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "s", "e", "w"]}, #07,96,00 / #77

         {"name":"AERODROME HIGHWAY NORTH (200 BLOCK)",
           "description":"Aerodrome Highway is a large, busy road running north and south through Red City, the Capital of Acadia.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["s"]}, #07,97,00 / #78

         {"name":"AERODROME HIGHWAY SOUTH (100 BLOCK)",
           "description":"Aerodrome Highway is a large, busy road running north and south through Red City, the Capital of Acadia.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["n", "s"]}, #07,94,00 / #79

         {"name":"EVANGELINE DOWNS HORSETRACK",
           "description":"There are horses and trainers everywhere. It smells like a stable.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["w"]}, #02,98,00 / #80

         {"name":"ACADIA KINGDOM UNIVERSITY",
           "description":"The largest educational institute in the kingdom, AKU is where all of the best Voodoo Mambos studied.",
           "npc":[9], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["n"]}, #07,93,00 / #81

         {"name":"TIGER STADIUM",
           "description":"AKU holds sporting events in this giant stadium.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #06,94,00 / #82

         {"name":"WALK-ONS",
           "description":"AKU tailgaters often end up here after sporting events.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["w"]}, #08,94,00 / #83

         {"name":"ACADIA CASTLE",
           "description":"King Drewberry Breeze of Acadia lives here along with his royal court. All business must come through the King's officials.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #06,96,00 / #84

         {"name":"ACADIA HIGHWAYMEN TROOP A",
           "description":"The main HQ of the Highwaymen is huge and noisy. Only the most experienced highwaymen in the kingdom get stationed here.",
           "npc":[6], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["w"]}, #08,96,00 / #85
         
         {"name":"RED CITY SHERIFF'S HQ",
           "description":"The Red City Sheriff and his deputies handle all of the peacekeeping and tax collection within the city limits.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #06,97,00 / #86

         {"name":"ACADIA AERODROME",
           "description":"A giant field of runways and launchpads with all sorts of flying vehicles coming and going.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["w"]}, #08,97,00 / #87

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["n", "e"]}, #06,98,00 / #88

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["n" "s", "e", "w"]}, #07,98,00 / #89

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["n", "w"]}, #08,98,00 / #90

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["n", "s", "e"]}, #06,99,00 / #91

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["n" "s", "e", "w"]}, #07,99,00 / #92

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["n", "s", "w"]}, #08,99,00 / #93

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds. The Vermilion swamp is to the west, and the mighty Miss Sippy River is to the north.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["s", "e", "w"]}, #06,00,00 / #94

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds. The mighty Miss Sippy River is to the north.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["s", "e", "w"]}, #07,00,00 / #95

         {"name":"SHERWOOD FOREST",
           "description":"This dark and dense forest is full of strange sounds. The mighty Miss Sippy River is to the north.",
           "npc":[], "mob":[3], "mob_chance":[0.1], "mob_max":[3], "room_level":1, "room_type":1,
           "exits":["s", "w"]}, #08,00,00 / #96

         {"name":"THE UNIVERSITY OF ACADIA AT VERMILIONVILLE",
           "description":"Although not as large or prestigious as the Kingdom of Acadia University, UAV produces Voodoos and Mambos that can certainly hold their own in a magic battle. Cajun Field and the Cajundome are further west.",
           "npc":[8], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #00,98,00 / #97

         {"name":"CAJUN FIELD",
           "description":"Home of the Ragin' Cajuns! The University is to the east and the Cajundome is to the west.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":1,
           "exits":["e", "w"]}, #99,98,00 / #98

         {"name":"THE CAJUNDOME",
           "description":"Not nearly as large as Tiger Stadium in Red City, the Cajundome at least provides an indoor venue for events. The Cajun Chicken is running around, clucking loudly. The Univerity and Cajun Field are to the east.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["e"]}, #98,98,00 / #99

         {"name":"ST. JOHN'S CATHEDRAL",
           "description":"Dozens of Catholics are sitting and quietly praying inside this tall and stately cathedral. Outside a giant oak tree stands guard over the cemetary.",
           "npc":[], "mob":[], "mob_chance":[], "mob_max":[], "room_level":1, "room_type":0,
           "exits":["s"]}, #01,03,00 / #100
         
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

    def mob_possible(self):
        if self.mob:
            return True
        else:
            return False

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


            
