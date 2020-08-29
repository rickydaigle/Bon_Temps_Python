#!/usr/bin/env python3

# Python Module Imports
import os
from pathlib import Path

# Local Module Imports
from actors.player import Player
from actors.mob import Mob
from actors.npc import Npc
from maps.map import Map
from items.weapons import Weapons
from items.armor import Armor
from items.items import Items
from output.art import *
from output.printer import Printer
from features.highscores import Scores
from features.saveload import Saveload
from features.battlesystem import Battle

# File Location Constants
SAVE_LOCATION = Path(os.getcwd() + "\\saves")
HIGH_SCORES_LOCATION = Path(os.getcwd() + "\\features\\highscores.dat")
HELP_LOCATION = Path(os.getcwd() + "\\output")

# In-Game Menu Logic
# QUIT

def start_game(player):
    gameRunning = True
    while gameRunning:
        if player.player_alive():
            playerName = player.get_name()
            x, y, z = player.get_location()
            room = Map(x, y, z)
            npcList = room.return_npcs()
            npcs = check_for_npcs(npcList)
            mobs, mobIds = check_for_mobs(room)
            choice = Printer.game_menu(player, room, npcs, mobs)
            if choice.lower() == "quit":
                Printer.back_to_main()
                gameRunning = False
            elif choice.lower() == "help":
                Printer.print_help()
            elif choice.lower() == "save":
                save_this_game(SAVE_LOCATION, playerName, player.pack_data())
            elif choice.lower() == "stats":
                collect_all_stats(player)
            elif choice.lower() == "inventory":
                check_inventory(player)          
            elif (choice.lower() == "n" or choice.lower() == "s" or choice.lower() == "e" or
                  choice.lower() == "w" or choice.lower() == "u" or choice.lower() == "n"):
                newX, newY, newZ = update_player_location(choice)
                player.update_location(newX, newY, newZ)
            if mobIds:
                if choice in mobIds:
                    interact_with_mob(mobs[int(choice)-1], player)
            if npcs:
                if choice.lower() in npcList:
                    get_npc_options(choice, player)
        else:
            gameRunning = False
            Printer.game_over(player)

def check_item_type(item):
    armorNames = []
    itemType = False
    for each in Armor.ARMOR:
        armorNames.append(each.lower())
    if item.lower() in armorNames:
        itemType = "armor"
    weaponNames = []
    for each in Weapons.WEAPONS:
        weaponNames.append(each.lower())
    if item.lower() in weaponNames:
        itemType = "weapon"
    otherNames = []
    for each in Items.ITEMS:
        otherNames.append(each.lower())
    if item.lower() in otherNames:
        itemType = "item"
    return itemType

def check_inventory(player):
    invList = player.check_inventory()
    if invList:
        itemUsed = Printer.inventory_select(invList)
        if itemUsed:
            itemType = check_item_type(itemUsed)
            if itemType:
                if itemType == "armor":
                    armorName = Armor.get_real_name(itemUsed)
                    if armorName:
                        player.gain_armor(armorName)
                        player.remove_inventory(armorName)
                elif itemType == "item":
                    itemName = Items.get_real_name(itemUsed)
                    if itemName:
                        Items.use_item(itemName, player)
                        player.remove_inventory(itemName)
                elif itemType == "weapon":
                    weaponName = Weapons.get_real_name(itemUsed)
                    if weaponName:
                        attackVerb, defenseVerb = Weapons.get_actions(weaponName)
                        player.gain_weapon(weaponName, attackVerb, defenseVerb)
                        player.remove_inventory(weaponName)
            else:
                Printer.something_wrong()
    else:
        Printer.inv_empty()

def check_for_classes(player, itemClass):
    playerClass = player.get_class()
    useClasses = ["newb"]
    if playerClass == "hunter":
        useClasses.append(playerClass)
    elif playerClass == "voodoo":
        useClasses.append(playerClass)
    elif playerClass == "hero":
        useClasses.append(playerClass, "hunter")
    elif playerClass == "mambo":
        useClasses.append(playerClass, "voodoo")
    elif playerClass == "master":
        useClasses.append(playerClass, "hunter", "voodoo")
    if itemClass in useClasses:
        return True
    else:
        return False

def get_npc_options(name, player):
    itemPage = False
    npcType = Npc.NPC_LIST[str(name)]["type"]
    npcWelcome =Npc.NPC_LIST[str(name)]["welcome"]
    if npcType == "weapons":
        itemPage = Weapons.WEAPONS
    elif npcType == "armor":
        itemPage = Armor.ARMOR
    elif npcType == "items":
        itemPage = Items.ITEMS
    elif npcType == "quest":
        print("\n{} says {}".format(name.capitalize(), npcWelcome)) # REMOVE
        print("You're not sure about this guy yet, so you ignore him.") # REMOVE
    waresList = []
    if itemPage:
        for e, each in enumerate(itemPage):
            newWare = []
            newWare.append(e+1)
            newWare.append(str(each))
            newWare.append(itemPage[each]["value"])
            newWare.append(itemPage[each]["desc"])
            waresList.append(newWare)
        itemBought = Printer.talk_to_npc(name, player, waresList, npcWelcome)
        if itemBought:
            itemClass = itemPage[itemBought]["itemClass"]
            itemCost = itemPage[itemBought]["value"]
            if check_for_classes(player, itemClass):
                if player.check_currency(itemCost):
                    player.lose_currency(itemCost)
                    player.add_inventory(itemBought)
                    Printer.item_bought(itemBought)
                else:
                    Printer.cant_afford()
            else:
                Printer.cant_use()

def interact_with_mob(mob, player):
    battle = Printer.mob_choices(mob, player)
    if battle:
        start_battle(mob, player)

def start_battle(mob, player):
    weaponName = player.get_weapon()
    armorName = player.get_armor()
    if weaponName == "Fists":
        weaponAttack = 0
        weaponDefense = 0
    else:
        weaponAttack = Weapons.WEAPONS[weaponName]["attack"]
        weaponDefense = Weapons.WEAPONS[weaponName]["defense"]
    if armorName == "Cotton Draws":
        armorDefense = 0
    else:
        armorDefense = Armor.ARMOR[armorName]["defense"]
    totalAttack, totalDefense = calculate_battle_stats(player, weaponAttack, weaponDefense, armorDefense)
    Battle.begin_battle(player, mob, totalAttack, totalDefense)

def collect_all_stats(player):
    baseAttack = player.get_attack()
    baseDefense = player.get_defense()
    weaponName = player.get_weapon()
    armorName = player.get_armor()
    if weaponName == "Fists":
        weaponAttack = 0
        weaponDefense = 0
    else:
        weaponAttack = Weapons.WEAPONS[weaponName]["attack"]
        weaponDefense = Weapons.WEAPONS[weaponName]["defense"]
    if armorName == "Cotton Draws":
        armorDefense = 0
    else:
        armorDefense = Armor.ARMOR[armorName]["defense"]
    totalAttack, totalDefense = calculate_battle_stats(player, weaponAttack, weaponDefense, armorDefense)
    Printer.print_stats(player, weaponAttack, weaponDefense, armorDefense, totalAttack, totalDefense)

def calculate_battle_stats(player, weaponAttack, weaponDefense, armorDefense):
    baseAttack = player.get_attack()
    baseDefense = player.get_defense()
    totalAttack = baseAttack + weaponAttack
    totalDefense = baseDefense + weaponDefense + armorDefense
    return totalAttack, totalDefense  

def save_this_game(SAVE_LOCATION, playerName, playerData):
    Saveload.save_game(SAVE_LOCATION, playerName, playerData)
    if Saveload.check_for_save(SAVE_LOCATION, playerName):
        Printer.save_successful(playerName)
    else:
        Printer.something_wrong()

def update_player_location(direction):
    x, y, z = 0, 0, 0
    if direction.lower() == "n":
        y = 1
    elif direction.lower() == "s":
        y = -1
    elif direction.lower() == "e":
        x = 1
    elif direction.lower() == "w":
        x = -1      
    elif direction.lower() == "u":
        z = 1
    elif direction.lower() == "d":
        z = -1
    return x, y, z

def check_for_npcs(npcList):
    if npcList:
        npcs = []
        for npc in npcList:
            newNpc = []
            newNpc.append(str(npc))
            newNpc.append(Npc.NPC_LIST[str(npc)]["desc"])
            newNpc.append(Npc.NPC_LIST[str(npc)]["welcome"])
            npcs.append(newNpc)
        return npcs
    else:
        return False

def check_for_mobs(room):
    mobList = room.return_mobs()
    if mobList:
        mobs = []
        mobIds = []
        for d, mob in enumerate(mobList):
            newMob = Mob(mob, d + 1)
            mobs.append(newMob)
            mobIds.append(str(d + 1))
        return mobs, mobIds
    else:
        return False, False


# Main Menu Logic
#----------------
# START New Game
# LOAD Saved Game
# LIST Saved Games
# DELETE Saved Game
# READ Instructions
# VIEW High Scores
# QUIT

def main():
    highScores = Scores.populate_high_scores(HIGH_SCORES_LOCATION)
    applicationRunning = True
    Art.print_art(mainTitleLogo)
    while applicationRunning:
        choice = Printer.main_menu()
        if choice.lower() == "quit":
            applicationRunning = False
        elif choice.lower() == "view":
            view_high_scores(highScores)
        elif choice.lower() == "read":
            read_instructions(HELP_LOCATION)
        elif choice.lower() == "list":
            list_saved_games(SAVE_LOCATION)
        elif choice.lower() == "load":
            load_saved_game(SAVE_LOCATION)
        elif choice.lower() == "delete":
            delete_saved_game(SAVE_LOCATION)
        elif choice.lower() == "start":
            start_new_game(SAVE_LOCATION)
    quit_game()

def quit_game():
    print("\nThanks for playing!\n")

def view_high_scores(highScores):
    maxScoreLen, maxNameLen = Scores.get_max_lengths(highScores)
    Printer.print_high_scores(highScores, maxScoreLen, maxNameLen)
    
def read_instructions(HELP_LOCATION):
    Printer.print_instructions(HELP_LOCATION)

def list_saved_games(SAVE_LOCATION):
    listOfNames = Saveload.return_all_saved_games(SAVE_LOCATION)
    Printer.print_all_saves(listOfNames)

def load_saved_game(SAVE_LOCATION):
    loadName = Printer.load_game(SAVE_LOCATION)
    playerData = Saveload.load_game(SAVE_LOCATION, loadName)
    if playerData:
        playerName = playerData["name"]
        player = Player(playerName)
        player.unpack_data(playerData)
        start_game(player)
    else:
        Printer.not_found()
    
def delete_saved_game(SAVE_LOCATION):
    deletePlayer = Printer.delete_saved_game(SAVE_LOCATION)
    if Saveload.check_for_save(SAVE_LOCATION, deletePlayer):
        if Printer.confirm_delete(deletePlayer):
            if Saveload.delete_this_player(SAVE_LOCATION, deletePlayer):
                Printer.player_deleted(deletePlayer)
            else:
                Printer.something_wrong()
    else:
        Printer.not_found()

def start_new_game(SAVE_LOCATION):
    playerName = Printer.get_new_player(SAVE_LOCATION)
    playerData = Saveload.load_game(SAVE_LOCATION, playerName)
    if playerData:
        Printer.already_exists()
    else:
        player = Player(playerName)
        start_game(player)
    

if __name__ == "__main__":
    main()
