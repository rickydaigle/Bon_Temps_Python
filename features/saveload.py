#!/usr/bin/env python3

# This module allows for save & load functionality

# To use this module:
# 1.) from features.SaveLoad import saveload
# 2.) create a constant such as SAVE_LOCATION to store the save files
#   - this can be done using Path:
#       from pathlib import Path
#       SAVE_LOCATION = Path(os.getcwd() + "\\saves\\")
# 3.) use class functions as needed - pretty straightforward


import pickle
import os

class Saveload:

    def save_game(SAVE_LOCATION, playerName, playerData):
        """
        Saves the player data to a file named after the player.
        @param SAVE_LOCATION - the directory location of save files
        @param playerName - the name of the player
        @param playerData - the player data
        """
        saveName = playerName.lower() + ".dat"
        with open(str(SAVE_LOCATION) + "\\" + saveName, "wb") as f:
            pickle.dump(playerData, f, protocol = pickle.HIGHEST_PROTOCOL)

    def load_game(SAVE_LOCATION, playerName):
        """
        Loads the player data.
        @param SAVE_LOCATION - the directory location of save files
        @param playerName - the name of the player
        @return playerData - returns the player data if file found, otherwise returns False
        """
        if Saveload.check_for_save(SAVE_LOCATION, playerName):
            loadName = playerName.lower() + ".dat"
            with open(str(SAVE_LOCATION) + "\\" + loadName, "rb") as f:
                playerData = pickle.load(f)
            return playerData
        else:
            return False

    def return_all_saved_games(SAVE_LOCATION):
        """
        Returns a list of saved file names from a list of all files in a directory.
        @param SAVE_LOCATION - the directory location of save files
        @return listOfNames - returns a list of all file names
        """
        nameList = Saveload.get_all_saves(SAVE_LOCATION)
        listOfNames = []
        for each in nameList:
            if ".dat" in each:
                with open(str(SAVE_LOCATION) + "\\" + each, "rb") as f:
                    listOfNames.append(each)
        return listOfNames           
            
    def check_for_save(SAVE_LOCATION, playerName):
        """
        Checks for a save file.
        @param SAVE_LOCATION - the directory location of save files
        @param playerName - the name of the player
        @return True if player data found, False if not
        """
        for entry in os.listdir(SAVE_LOCATION):
            if entry == playerName.lower() + ".dat":
                return True
        return False

    def get_all_saves(SAVE_LOCATION):
        """
        Gets all file names in a directory.
        @param SAVE_LOCATION - the directory location of save files
        @return nameList - all files in a directory, valid saves or not
        """
        nameList = os.listdir(SAVE_LOCATION)
        return nameList

    def delete_this_player(SAVE_LOCATION, playerName):
        """
        Deletes a save file.
        @param SAVE_LOCATION - the directory location of save files
        @param playerName - the name of the player
        @return True if player data found, False if not
        """
        if Saveload.check_for_save(SAVE_LOCATION, playerName):
            deleteFile = str(SAVE_LOCATION) + "\\" + str(playerName.lower()) + ".dat"
            os.remove(deleteFile)
            return True
        else:
            return False

def unit_test():
    from pathlib import Path
    SAVE_LOCATION = os.getcwd() + "\\"
    playerName = "Ricky"
    playerData = {"name":"Ricky", "level":1}
    print("Saving ricky.dat")
    Saveload.save_game(SAVE_LOCATION, playerName, playerData)
    gameFound = Saveload.check_for_save(SAVE_LOCATION, playerName)
    print("Found ricky.dat? {}".format(str(gameFound)))
    playerName = "Suzy"
    playerData = {"name":"Suzy", "level":2}
    print("Saving suzy.dat")
    Saveload.save_game(SAVE_LOCATION, playerName, playerData)
    gameFound = Saveload.check_for_save(SAVE_LOCATION, playerName)
    print("Found suzy.dat? {}".format(str(gameFound)))
    listOfNames = Saveload.return_all_saved_games(SAVE_LOCATION)
    print("All saves found:")
    for each in listOfNames:
        print(str(each))
    print("Deleting Ricky...")
    Saveload.delete_this_player(SAVE_LOCATION, "Ricky")
    listOfNames = Saveload.return_all_saved_games(SAVE_LOCATION)
    print("All saves found:")
    for each in listOfNames:
        print(str(each))
    print("Deleting all files...")
    Saveload.delete_this_player(SAVE_LOCATION, "Suzy")
    input("Press Enter to exit test...")

if __name__ == "__main__":
    unit_test()

