#!/usr/bin/env python3

import re
import os
import textwrap
from collections import Counter

class Printer:

    def print_pounds():
        print("#" * 45)

    def print_long_pounds():
        print("#" * 90)

    def print_stars():
        print("*" * 45)

    def print_dashes():
        print("-" * 45)

    def print_long_dashes():
        print("-" * 90)

    def print_lines():
        print("_" * 45)

    def invalid_choice():
        print("\n|| That isn't an option, please try again.\n")

    def not_found():
        print("\n|| That file was not found.")

    def wait_for_input():
        ready = input("\nPress Enter to continue...")

    def already_exists():
        print("\n|| That player already exists. Try loading a saved game.")
        Printer.wait_for_input()

    def item_bought(itemBought):
        print("\n|| {} purchased.".format(itemBought))

    def inv_empty():
        print("\n|| There is nothing in your inventory.")
        Printer.wait_for_input()

    def cant_afford():
        print("\n|| Sorry, you can't afford that.")
        Printer.wait_for_input()

    def cant_use():
        print("\n|| Sorry, your class can't buy that.")
        Printer.wait_for_input()

    def back_to_main():
        print("\n|| Quitting to main menu...")

    def place_value(number):
        return ("{:,}".format(number))

    def something_wrong():
        print("\n|| Sorry, something went wrong. Operation cancelled.")

    def game_over(player):
        print("\n{} is dead. Sorry. (I hope you saved your game!)".format(player.get_name()))
        Printer.wait_for_input()

    def save_successful(playerName):
        print("\n|| {} saved successfully!".format(playerName))

    def print_high_scores(highScores, maxScoreLen, maxNameLen):
        rankJust = 6
        nameJust = 2
        scoreJust = 2        
        print("\nHIGH SCORES - (Local Players)")
        Printer.print_stars()
        print("Rank".ljust(rankJust) + "Name".ljust(maxNameLen + nameJust) + "Score".ljust(maxScoreLen + scoreJust))
        Printer.print_dashes()
        for rank, each in enumerate(highScores):
            print(str(rank+1).ljust(rankJust) + str(each["name"]).ljust(maxNameLen + nameJust) + str(Printer.place_value(each["score"]).ljust(maxScoreLen + scoreJust)))
        Printer.print_stars()
        Printer.wait_for_input()

    def print_stats(player, weaponAttack, weaponDefense, armorDefense, totalAttack, totalDefense):
        print()
        Printer.print_pounds()
        print(str(player.print_name_title()))
        print("Level          : {} | {} to next level".format(player.get_level(), player.points_to_level()))
        playerClass = player.get_class()
        print("Current Class  : {}".format(playerClass.capitalize()))
        Printer.print_dashes()
        print("Armor          : {}".format(player.get_armor()))
        print("Weapon         : {}".format(player.get_weapon()))
        print("Armor Defense  : {}".format(armorDefense))
        print("Weapon Attack  : {} | Weapon Defense: {}".format(weaponAttack, weaponDefense))
        print("Base Attack    : {} | Base Defense  : {}".format(player.get_attack(), player.get_defense()))
        print("Total Attack   : {} | Total Defense : {}".format(totalAttack, totalDefense))
        Printer.print_dashes()
        print("Lifetime Kills : {}".format(player.get_total_kills()))
        print("Bones Earned   : {}".format(player.get_total_currency()))
        print("Clues Found    : {}".format(player.get_total_clues()))
        Printer.print_pounds()
        Printer.wait_for_input()
        
    def print_instructions(HELP_LOCATION):
        print()
        print("\nAbout the game:")
        Printer.print_stars()
        if os.path.isfile(str(HELP_LOCATION) + "\\about_game.txt"):
            textFile = open(str(HELP_LOCATION) + "\\about_game.txt", "r")
            aboutGame = textFile.read()
            textFile.close()
            print(textwrap.fill(aboutGame, 60))
        else:
            print("Error: instruction file 'about_game.txt' not found")
        print("\nHow to play:")
        Printer.print_stars()
        if os.path.isfile(str(HELP_LOCATION) + "\\how_to_play.txt"):
            textFile = open(str(HELP_LOCATION) + "\\how_to_play.txt", "r")
            howToPlay = textFile.read()
            textFile.close()
            print(textwrap.fill(howToPlay, 60))
        else:
            print("Error: instruction file 'how_to_play.txt' not found")
        Printer.wait_for_input()

    def print_help():
        file_dir = os.getcwd() + "\\output"
        print()
        Printer.print_lines()
        print("\nMovement")
        Printer.print_stars()
        if os.path.isfile(file_dir + "\\game_movement.txt"):
            text_file = open(file_dir + "\\game_movement.txt", "r")
            about_game = text_file.read()
            text_file.close()
            print(textwrap.fill(about_game, 60))
        else:
            print("Error: instruction file 'game_movement.txt' not found")
        print("\nActions")
        Printer.print_stars()
        if os.path.isfile(file_dir + "\\game_actions.txt"):
            text_file = open(file_dir + "\\game_actions.txt", "r")
            about_game = text_file.read()
            text_file.close()
            print(textwrap.fill(about_game, 60))
        else:
            print("Error: instruction file 'game_actions.txt' not found")
        Printer.print_lines()
        Printer.wait_for_input()

    def print_all_saves(listOfNames):
        if listOfNames:
            print("\nThe following saved games were found:")
            for each in listOfNames:
                print(str(each))
        else:
            print("\nNo saved games were found.")
        Printer.wait_for_input()

    def load_game(SAVE_LOCATION):
        loadName = input("\nWhat game do you want to load? ")
        return loadName.lower()

    def delete_saved_game(SAVE_LOCATION):
        deleteName = input("\nWhat game do you want to delete? ")
        return deleteName.lower()

    def confirm_delete(deletePlayer):
        confirm = input("Are you sure you want to delete {}? (y/n) ".format(deletePlayer))
        if confirm.lower() == "y" or confirm.lower() == "yes":
            return True
        else:
            return False

    def player_deleted(deletePlayer):
        print("\n|| {}.dat was deleted.".format(deletePlayer))
        Printer.wait_for_input()

    def get_new_player(SAVE_LOCATION):
        validated = False
        regex = re.compile("[^a-z A-Z '-]")
        while validated == False:
            playerName = input("\nName your new character: ")
            playerName = playerName.strip()
            playerName = regex.sub("", playerName)
            confirm = input("Is {} correct? (y/n) ".format(playerName))
            if confirm.lower() == "y" or confirm.lower() == "yes":
                return playerName
            else:
                print("Well what IS it then?")

    def exits_to_string(exits):
        exitString = ""
        for each in exits:
            if each.lower() == "n":
                exitString += "(N)orth "
            elif each.lower() == "e":
                exitString += "(E)ast "
            elif each.lower() == "s":
                exitString += "(S)outh "
            elif each.lower() == "w":
                exitString += "(W)est "
            elif each.lower() == "u":
                exitString += "(U)p "
            elif each.lower() == "d":
                exitString += "(D)own "
        exitString.strip()
        return exitString

    def get_max_lengths(shopData):
        """
        Returns the length of the longest values of name and value in the shop data list.
        @param shopData - the shop data (list of lists)
        @returns maxNameLen - the number of characters in the longest name
        @returns maxValueLen - the number of characters in the longest value
        """
        maxNameLen = 0
        maxValueLen = 0
        for each in shopData:
            if len(each[1]) > maxNameLen:
                maxNameLen = len(each[1])
            if len(str(each[2])) > maxValueLen:
                maxValueLen = len(str(each[2]))
        return maxNameLen, maxValueLen

    def print_shop_format(shopData, itemJust, nameJust, valueJust):
        maxNameLen, maxValueLen = Printer.get_max_lengths(shopData)
        itemNames = []
        totalItems = []
        print("#".ljust(itemJust) + "Name".ljust(maxNameLen + nameJust) + "Cost".ljust(maxValueLen + valueJust) + "Description")
        Printer.print_long_dashes()
        e = 0
        for each in shopData:
            e += 1
            print(str(each[0]).ljust(itemJust) + str(each[1]).ljust(maxNameLen + nameJust) + str(each[2]).ljust(maxValueLen + valueJust) + str(each[3]))
            totalItems.append(str(e))
            itemNames.append(each[1])
        return totalItems, itemNames

    def talk_to_npc(name, player, wares, npcWelcome):
        validated = False
        valid_choices = ["cancel"]
        print("\n{} says '{}'".format(name.capitalize(), npcWelcome))
        itemJust = 4
        nameJust = 2
        valueJust = 4
        Printer.print_long_pounds()
        totalItems, itemNames = Printer.print_shop_format(wares, itemJust, nameJust, valueJust)
        for each in totalItems:
            valid_choices.append(each[0])
        Printer.print_long_pounds()
        print("Type the # of the item you want to buy or CANCEL to close this menu.")
        while validated == False:
            choice = input("What do you want to do? ")
            if choice.lower() in valid_choices:
                if choice.lower() == "cancel":
                    validated = True
                    return False
                else:
                    actualChoice = itemNames[int(choice)-1]
                    validated = True
                    return actualChoice
            else:
                Printer.invalid_choice()

    def get_all_lower(upperList):
        lowerList = []
        for each in upperList:
            lowerList.append(each.lower())
        return lowerList

    def inventory_select(invList):
        validated = False
        print()
        Printer.print_pounds()
        lowerList = Printer.get_all_lower(invList)
        invCounted = Counter(invList)
        print("Current inventory:")
        Printer.print_dashes()
        for key, value in invCounted.items():
            if value > 1:
                print("{} x {}".format(key, value))
            else:
                print("{}".format(key))
        Printer.print_pounds()
        while validated == False:
            choice = input("Select an item to use or type CANCEL: ")
            if choice.lower() == "cancel":
                validated = True
                return False
            elif choice.lower() in lowerList:
                validated = True
                return choice
            else:
                print(invList)
                print(choice)
                print(choice.lower())
                Printer.invalid_choice()
        

    def main_menu():
        validated = False
        print("\nWelcome to BonTemps!")
        Printer.print_pounds()
        valid_choices = ["start", "load", "list", "delete", "read", "view", "quit"]
        print("START a New Game")
        print("LOAD a Saved Game")
        print("LIST the Saved Games")
        print("DELETE a Saved Game")
        print("READ the Instructions")
        print("VIEW High Scores")
        print("QUIT")
        Printer.print_pounds()
        while validated == False:
            choice = input("What do you want to do? ")
            if choice.lower() in valid_choices:
                validated = True
                return choice
            else:
                Printer.invalid_choice()

    def game_menu(player, room, npcs, mobs):
        validated = False
        valid_choices = ["help", "save", "quit", "stats", "inventory"]
        print()
        Printer.print_pounds()
        print("{} | HP:{} | XP:{}/{} | ${}".format(
            player.get_name(),
            player.get_health(),
            player.get_exp(),
            player.get_expcap(),
            player.get_currency()))
        Printer.print_dashes()
        print("Your location: {}".format(room.print_name()))
        roomDesc = str(room.print_description())
        print(textwrap.fill(roomDesc, 45))
        print("   Exits: {}".format(Printer.exits_to_string(room.return_exits())))
        Printer.print_stars()
        if npcs:
            print("You can interact with:")
            for npc in npcs:
                name = npc[0]
                print("   {} {}".format(name.capitalize(), npc[1]))
                valid_choices.append(name.lower())
            Printer.print_stars()
        if mobs:
            print("There are enemies here!:")
            for mob in mobs:
                mobId = mob.get_id()
                print("   #{} - A {} is nearby.".format(mobId, mob.print_name()))
                valid_choices.append(str(mobId))
            Printer.print_stars()
        for exits in room.return_exits():
            valid_choices.append(exits)
        print("INVENTORY check")
        print("STATS check")
        print("HELP text")
        print("SAVE your Game")
        print("QUIT")
        Printer.print_pounds()
        while validated == False:
            choice = input("What do you want to do? ")
            if choice.lower() == "inv":
                choice = "inventory"
            if choice.lower() in valid_choices:
                validated = True
                return choice
            else:
                Printer.invalid_choice()

    def mob_choices(mob, player):
        interacting = True
        while interacting == True:
            valid_choices = ["examine", "attack", "cancel"]
            Printer.print_pounds()
            print("\nYou see a {}.".format(mob.print_name()))
            print("EXAMINE it")
            print("ATTACK it")
            print("CANCEL")
            Printer.print_pounds()
            validated = False
            while validated == False:
                choice = input("What do you want to do? ")
                if choice.lower() in valid_choices:
                    if choice.lower() == "examine":
                        Printer.examine_mob(mob, player)
                        validated = True
                    elif choice.lower() == "attack":
                        validated = True
                        interacting == False
                        return True
                    elif choice.lower() == "cancel":
                        validated = True
                        interacting == False
                        return False                    
                    else:
                        Printer.something_wrong()
                else:
                    Printer.invalid_choice()

    def examine_mob(mob, player):
        mobLevel = mob.get_level()
        mobAttack = mob.get_attack()
        mobDefense = mob.get_defense()
        playerLevel = player.get_level()
        playerAttack = player.get_attack()
        playerDefense = player.get_defense()
        levelDiff = abs(playerLevel - mobLevel)
        attackDiff = abs(playerAttack - mobAttack)
        defenseDiff = abs(playerDefense - mobDefense)
        print("\nYou study the {}...".format(mob.print_name()))
        if levelDiff < 1:
            print("Your level seems about the same.")
        elif levelDiff < 3:
            if playerLevel > mobLevel:
                print("Your level seems higher.")
            else:
                print("Your level seems lower.")
        else:
            if playerLevel > mobLevel:
                print("Your level seems much higher.")
            else:
                print("Your level seems much lower.")     
        if attackDiff < 3:
            print("Your attack power seems about the same.")
        elif attackDiff < 3:
            if playerAttack > mobAttack:
                print("Your attack power seems higher.")
            else:
                print("Your attack power seems lower.")
        else:
            if playerAttack > mobAttack:
                print("Your attack power seems much higher.")
            else:
                print("Your attack power seems much lower.")
        if defenseDiff < 3:
            print("Your defense power seems about the same.")
        elif defenseDiff < 3:
            if playerDefense > mobDefense:
                print("Your defense power seems higher.")
            else:
                print("Your defense power seems lower.")
        else:
            if playerDefense > mobDefense:
                print("Your defense power seems much higher.")
            else:
                print("Your defense power seems much lower.")
        Printer.wait_for_input()

def unit_test():
        pass
             
if __name__ == "__main__":
    unit_test()
