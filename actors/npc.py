#!/usr/bin/env python3

class Npc:

    NPC_LIST = {
        "patackus":{"desc":"an old man", "type":"quest", "welcome":"Come see over here T, you look like you lost."},
        "amos":{"desc":"the Blacksmith", "type":"weapons", "welcome":"Hey cuz, you interested in a new weapon?"},
        "swiff":{"desc":"the Tailor", "type":"armor", "welcome":"We got the finest clothes in Acadia, bruh!"},
        "jables":{"desc":"of the Dee", "type":"items", "welcome":"I got the hottest links and the best prices, me!"},
        "morris":{"desc":"Bart", "type":"quest", "welcome":"One call, that's all!"}
        }
    
    def print_desc(npc):
        return Npc.NPC_LIST[npc]["desc"]

    def print_welcome(npc):
        return Npc.NPC_LIST[npc]["welcome"]

    def get_type(npc):
        return Npc.NPC_LIST[npc]["type"]

    def get_currency(npc):
        return self.currency
