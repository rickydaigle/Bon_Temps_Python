#!/usr/bin/env python3

# This module allows for a 10-slot high score list

# To use this module:
# 1.) from features.highscores import Scores
# 2.) create a constant such as HIGH_SCORES_LOCATION to store the high scores file location
#   - this can be done using Path:
#       from pathlib import Path
#       HIGH_SCORES_LOCATION = Path(os.getcwd() + "\\scores.dat")
# 3.) generate the initial high score file by calling populate_high_scores and passing the file location
#   - highScores = Scores.populate_high_scores(HIGH_SCORES_LOCATION)
# 4.) check and update the scores as needed
#   - scoresUpdated = Scores.update_high_scores(highScores, playerName, playerScore, HIGH_SCORES_LOCATION)

import pickle
import os

class Scores:

    DEFAULT_SCORES = [
        {"score":1000,  "name":"Bobby Boucher"},
        {"score":2000,  "name":"Ignatius J. Reilly"},   
        {"score":3000,  "name":"Goody Robicheaux"},
        {"score":4000,  "name":"Chance Boudreaux"},
        {"score":5000,  "name":"Rene Lenier"},
        {"score":6000,  "name":"Luc Devreaux"},
        {"score":7000,  "name":"Etienne R. LaFitte"},
        {"score":8000,  "name":"Amos Moses"},
        {"score":9000,  "name":"Remy LeBeau"},
        {"score":10000, "name":"Beausoleil"}
        ]

    def populate_high_scores(scoresFileLocation):
        """
        Returns the High Scores from a file in the location passed to it.
        @param scoresFileLocation - the directory location of the High Scores file
        """
        # Ensure that the High Scores file exists
        Scores.check_for_high_scores(scoresFileLocation)
        # Load the scores from the file
        highScores = Scores.load_high_scores(scoresFileLocation)
        # Sort the scores from largest to smallest
        highScores.sort(reverse = True, key = Scores.sort_scores)
        # Return sorted list of scores
        return highScores

    def check_for_high_scores(scoresFileLocation):
        """
        If the High Scores file doesn't exist, creates the file.
        @param scoresFileLocation - the directory location of the High Scores file
        """
        if not scoresFileLocation.is_file():
            # Populate data from default scores
            scoreData = Scores.DEFAULT_SCORES
            # Create the scores file from the default data
            Scores.save_high_scores(scoreData, scoresFileLocation)

    def save_high_scores(scoreData, scoresFileLocation):
        """
        Saves the High Score data to a new High Scores file.
        @param scoreData - sorted list of scores
        @param scoresFileLocation - the directory location of the High Scores file
        """ 
        with open(scoresFileLocation, "wb") as f:
            pickle.dump(scoreData, f, protocol = pickle.HIGHEST_PROTOCOL)

    def load_high_scores(scoresFileLocation):
        """
        Loads High Scores from file and returns a list.
        @param scoresFileLocation - the directory location of the High Scores file
        """        
        with open(scoresFileLocation, "rb") as f:
            scoreData = pickle.load(f)
            return scoreData

    def sort_scores(e):
        """
        Sorts the list of High Scores by score.
        """      
        return e["score"]

    def check_for_existing_player(highScores, playerName):
        """
        Checks to see if a player is already in the High Score list.
        @param highScores - the High Score data
        @param playerName - the player name
        """   
        for x, each in enumerate(highScores):
            if each["name"] == playerName:
                return x
        return False

    def update_high_scores(highScores, playerName, playerScore, scoresFileLocation):
        """
        Updates the High Score list with the new High Scores and saves to file.
        @param highScores - the High Score data
        @param playerName - the player name
        @param playerScore - the player's score
        @param scoresFileLocation - the directory location of the High Scores file
        @returns updatedScores - True if scores were updated, False if not
        """
        updatedScores = False
        index = Scores.check_for_existing_player(highScores, playerName)
        minScore = highScores[-1]["score"]
        # If the player is already on the high score list...
        if index:
            oldScore = highScores[index]["score"]
            # If the player's score is larger than the previous score...
            if playerScore > oldScore:
                highScores[index]["score"] = newScore
                highScores[index]["name"] = playerName
                # If the player's new score moves them up a rank update the score and return True...
                if highScores[index]["score"] > highScores[index-1]["score"]:
                    highScores.sort(reverse = True, key = Scores.sort_scores)
                    updatedScores = True
                # ...update the score and return True
                else:
                    highScores.sort(reverse = True, key = Scores.sort_scores)
                    updatedScores = False
                Scores.save_high_scores(highScores, scoresFileLocation)
            else:
                updatedScores = False
        # If the player's score is greater than the lowest high score then replace the lowest ranked player & score
        elif playerScore >= minScore:
            highScores[-1]["name"] = playerName
            highScores[-1]["score"] = playerScore
            # Sort scores in case player's score put them in a higher rank than #10
            highScores.sort(reverse = True, key = Scores.sort_scores)
            Scores.save_high_scores(highScores, scoresFileLocation)
            updatedScores = True
        else:
            updatedScores = False
        return updatedScores

    def get_max_lengths(highScores):
        """
        Returns the length of the longest values of name and score in the high score list.
        @param highScores - the High Score data
        @returns maxScoreLen - the number of characters in the longest score
        @returns maxNameLen - the number of characters in the longest score
        """
        maxScoreLen = 0
        maxNameLen = 0
        for each in highScores:
            if len(each["name"]) > maxNameLen:
                maxNameLen = len(each["name"])
            if len(str(each["score"])) > maxScoreLen:
                maxScoreLen = len(str(each["score"]))
        return maxScoreLen, maxNameLen
            
def unit_test():
    from pathlib import Path
    HIGH_SCORES_LOCATION = Path(os.getcwd() + "\\TEST_highscores.dat")

    def print_shop_format(highScores, rankJust, nameJust, scoreJust):
        maxScoreLen, maxNameLen = Scores.get_max_lengths(highScores)
        print("Rank".ljust(rankJust) + "Name".ljust(maxNameLen + nameJust) + "Score".ljust(maxScoreLen + scoreJust))
        for rank, each in enumerate(highScores):
            print(str(rank+1).ljust(rankJust) + str(each["name"]).ljust(maxNameLen + nameJust) + str(each["score"]).ljust(maxScoreLen + scoreJust))
        print()
    
    print(str(HIGH_SCORES_LOCATION))
    highScores = Scores.populate_high_scores(HIGH_SCORES_LOCATION)
    for entry in os.listdir(Path(os.getcwd())):
        if entry == "TEST_highscores.dat":
            print("Existing file found - deleting...")
            deleteFile = str(HIGH_SCORES_LOCATION)
            os.remove(deleteFile)
    highScores = Scores.populate_high_scores(HIGH_SCORES_LOCATION)
    maxScoreLen, maxNameLen = Scores.get_max_lengths(highScores)
    rankJust = 6
    nameJust = 2
    scoreJust = 2
    print("Default High Scores:\n")
    print_shop_format(highScores, rankJust, nameJust, scoreJust)
    scoresUpdated = Scores.update_high_scores(highScores, "Pooty Pitpot", 1500, HIGH_SCORES_LOCATION)
    if scoresUpdated:
        print("New High Scores - Pooty Pitpot 1500:\n")
        print_shop_format(highScores, rankJust, nameJust, scoreJust)
    scoresUpdated = Scores.update_high_scores(highScores, "Nobody Nowhere", 1000, HIGH_SCORES_LOCATION)
    if scoresUpdated:
        print("IF YOU SEE THIS THEN SOMETHING WENT WRONG")
        print("New High Scores - Nobody Nowhere 1000:\n")
        print_shop_format(highScores, rankJust, nameJust, scoreJust)
    scoresUpdated = Scores.update_high_scores(highScores, "Ricky Daigle", 9000, HIGH_SCORES_LOCATION)
    if scoresUpdated:
        print("New High Scores - Ricky Daigle 9000:\n")
        print_shop_format(highScores, rankJust, nameJust, scoreJust)
    for entry in os.listdir(Path(os.getcwd())):
        if entry == "TEST_highscores.dat":
            print("Deleting test file...")
            deleteFile = str(HIGH_SCORES_LOCATION)
            os.remove(deleteFile)
    input("Press Enter to exit test...")
      
if __name__ == "__main__":
    unit_test()
    
