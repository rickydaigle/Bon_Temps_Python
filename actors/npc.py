#!/usr/bin/env python3

class Npc:

    NPC_LIST = {
        "patackus":{"desc":"an old man", "type":"quest", "classType":"", "welcome":"Come see over here T, you look like you lost. You should start out by heading 'nort' on da Evangeline 'Truway' to da cemetary and kill you some nutria. If you don't see 'anyting' at first, you can search da area and sometimes find 'em hidin'!"},
        "amos":{"desc":"the Blacksmith", "type":"weapons", "classType":"", "welcome":"Hey cuz, you interested in a new weapon?"},
        "swiff":{"desc":"the Tailor", "type":"armor", "classType":"", "welcome":"We got the finest clothes in Acadia, bruh!"},
        "jables":{"desc":"of the Dee", "type":"items", "classType":"", "welcome":"I got the hottest links and the best prices, me!"},
        "morris":{"desc":"Bart", "type":"quest", "classType":"", "welcome":"One call, that's all!"},
        "martin":{"desc":"Riggs", "type":"class", "classType":"hunter", "welcome":"Guys like you don't die in the cahbin."},
        "harry":{"desc":"Callahan", "type":"class", "classType":"hero", "welcome":"You feeling lucky, cuz?"},
        "john":{"desc":"McClain", "type":"class", "classType":"hero", "welcome":"Yippee Ki Yay, mere putain!"},
        "marie":{"desc":"Laveau", "type":"class", "classType":"voodoo", "welcome":"You wanna learn da Dark Arts, boo?."},
        "doctor":{"desc":"John", "type":"class", "classType":"mambo", "welcome":"Do you believe this is real?"}
        }
    
    def print_desc(npc):
        return Npc.NPC_LIST[npc]["desc"]

    def print_welcome(npc):
        return Npc.NPC_LIST[npc]["welcome"]

    def get_type(npc):
        return Npc.NPC_LIST[npc]["type"]

    def get_currency(npc):
        return self.currency
