#!/usr/bin/env python3

class Player:
   
    def __init__(self, name):
        self.name = name
        self.family = ""
        self.exp = 0
        self.expCap = 99
        self.level = 1
        self.maxHealth = 100
        self.health = 100
        self.attack = 5
        self.attackVerb = "punch"
        self.defense = 2
        self.defenseVerb = "block"
        self.defenseChance = 0.05
        self.currency = 0
        self.title = ""
        self.weapon = "Fists"
        self.armor = "Cotton Draws"
        self.playerClass = "newb"
        self.playerHeroMambo = False
        self.playerMaster = False
        self.isAlive = True
        self.lowHealth = False
        self.totalEarnings = 0
        self.totalKills = 0
        self.totalClues = 0
        self.currentLocation = {"x":0, "y":0, "z":0}
        self.inventory = []

    def check_class(self, className):
        if self.playerClass == "newb" and self.level > 2:
            if className == "hunter" or className == "voodoo":
                return True
            else:
                return False
        elif self.playerClass == "hunter" and className == "hero" and self.level > 9:
            return True
        elif self.playerClass == "voodoo" and className == "mambo" and self.level > 9:
            return True
        else:
            return False

    def new_class(self, className):
        self.playerClass = className

    def get_location(self):
        x = self.currentLocation["x"]
        y = self.currentLocation["y"]
        z = self.currentLocation["z"]
        return x, y, z

    def update_location(self, x, y, z):
        if x != 0:
            old_x = self.currentLocation["x"]
            new_x = old_x + x
            if new_x == -1:
                new_x = 99
            elif new_x == 100:
                new_x = 0
            self.currentLocation["x"] = new_x
        if y != 0:
            old_y = self.currentLocation["y"]
            new_y = old_y + y
            if new_y == -1:
                new_y = 99
            elif new_y == 100:
                new_y = 0
            self.currentLocation["y"] = new_y
        if z != 0:
            old_z = self.currentLocation["z"]
            new_z = old_z + z
            if new_z == -1:
                new_z = 99
            elif new_z == 100:
                new_z = 0
            self.currentLocation["z"] = new_z

    def check_titles(self):
        heroMambo = self.level > 9
        master = self.level > 24
        rich = self.totalEarnings > 999999
        killer = totalKills > 249
        return heroMambo, master, rich, killer

    def get_name(self):
        return str(self.name)

    def get_weapon(self):
        return self.weapon

    def get_armor(self):
        return self.armor

    def get_attack(self):
        return self.attack

    def get_attack_verb(self):
        return self.attackVerb

    def get_defense(self):
        return self.defense

    def get_defense_verb(self):
        return self.defenseVerb

    def get_defense_chance(self):
        return self.defenseChance

    def points_to_level(self):
        pointsNeeded = self.expCap - self.exp
        return pointsNeeded

    def get_level(self):
        return self.level

    def check_level(self):
        if self.exp > self.expCap:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.expCap += (self.expCap + int(round(self.expCap * 0.50)))
        self.maxHealth += (int(round(self.maxHealth * 0.15)))
        self.health = self.maxHealth
        self.attack += max(1, (int(round(self.attack * 0.25))))
        self.defense  += max(1,(int(round(self.defense * 0.25))))
        print("\nDING! You've reached a new level!")
        if self.level == "3" or self.level == "10":
            print("You should go talk to a class trainer now...")

    def player_alive(self):
        if self.isAlive == True:
            return True
        else:
            return False

    def player_dead(self):
        self.isAlive = False

    def player_low_health(self):
        if self.lowHealth == True:
            return True
        else:
            return False

    def get_total_kills(self):
        return self.totalKills

    def get_total_clues(self):
        return self.totalClues

    def get_total_currency(self):
        return self.totalEarnings

    def print_name(self):
        if self.family:
            fullName = str(self.name) + " " + str(self.family)
        else:
            fullName = str(self.name)
        return fullName

    def print_name_title(self):
        if self.family and self.title:
            return str(self.name + " " + self.family + " " + self.title)
        elif self.title:
            return str(self.name + " " + self.title)
        elif self.family:
            return str(self.name + " " + self.family)
        else:
            return self.name

    def get_exp(self):
        return self.exp

    def get_expcap(self):
        return self.expCap

    def get_currency(self):
        currency = str(int(self.currency))
        return currency

    def get_health(self):
        healthStatus = str(self.health) + "/" + str(self.maxHealth)
        return healthStatus

    def get_max_health(self):
        return self.maxHealth

    def get_stats(self):
        name = self.print_name_title()
        currency = self.get_currency()
        health = self.get_health()
        return name, self.level, health, self.attack, self.defense, self.exp, currency

    def gain_health(self, health):
        self.health += int(round(health))
        if self.health > self.maxHealth:
            self.health = self.maxHealth
            self.lowHealth = False
        elif self.health > (self.maxHealth * 0.2):
            self.lowHealth = False

    def lose_health(self, health):
        self.health -= int(round(health))
        if self.health <= 0:
            self.player_dead()
        elif self.health <= (self.maxHealth * 0.2):
            self.lowHealth = True

    def check_currency(self, amount):
        if amount > int(self.currency):
            return False
        else:
            return True

    def killed_enemy(self):
        self.totalKills += 1

    def gained_clue(self):
        self.totalClues += 1

    def gain_currency(self, currency):
        self.totalEarnings += int(currency)
        self.currency += int(currency)

    def lose_currency(self, currency):
        self.currency -= int(currency)
        if self.currency < 0:
            self.currency = 0

    def gain_exp(self, exp):
        self.exp += exp
        self.check_level()

    def gain_weapon(self, weapon, attackVerb, defenseVerb):
        self.weapon = weapon
        self.attackVerb = attackVerb
        self.defenseVerb = defenseVerb
        print("\n{} has been wielded!".format(weapon))

    def gain_armor(self, armor):
        self.armor = armor
        print("\n{} has been equipped!".format(armor))

    def lose_armor(self):
        self.armor = "Cotton Scraps"

    def get_class(self):
        return self.playerClass

    def player_heroMambo(self):
        if self.playerHeroMambo == True:
            return True
        else:
            return False

    def player_master(self):
        if self.playerMaster == True:
            return True
        else:
            return False

    def check_inventory(self):
        return self.inventory

    def add_inventory(self, item):
        self.inventory.append(item)

    def remove_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def pack_data(self):
        playerData = {
        "name":self.name,
        "family":self.family,
        "exp":self.exp,
        "expCap":self.expCap,
        "level":self.level,
        "maxHealth":self.maxHealth,
        "health":self.health,
        "attack":self.attack,
        "defense":self.defense,
        "currency":self.currency,
        "title":self.title,
        "weapon":self.weapon,
        "armor":self.armor,
        "playerClass":self.playerClass,
        "playerHeroMambo":self.playerHeroMambo,
        "playerMaster":self.playerMaster,
        "lowHealth":self.lowHealth,
        "totalEarnings":self.totalEarnings,
        "totalKills":self.totalKills,
        "totalClues":self.totalClues,
        "currentLocation":self.currentLocation,
        "inventory":self.inventory
        }
        return playerData

    def unpack_data(self, playerData):
        self.family = playerData["family"]
        self.exp = playerData["exp"]
        self.expCap = playerData["expCap"]
        self.level = playerData["level"]
        self.maxHealth = playerData["maxHealth"]
        self.health = playerData["health"]
        self.attack = playerData["attack"]
        self.defense = playerData["defense"]
        self.currency = playerData["currency"]
        self.title = playerData["title"]
        self.weapon = playerData["weapon"]
        self.armor = playerData["armor"]
        self.playerClass = playerData["playerClass"]
        self.playerHeroMambo = playerData["playerHeroMambo"]
        self.playerMaster = playerData["playerMaster"]
        self.lowHealth = playerData["lowHealth"]
        self.totalEarnings = playerData["totalEarnings"]
        self.totalKills = playerData["totalKills"]
        self.totalClues = playerData["totalClues"]
        self.currentLocation = playerData["currentLocation"]
        self.inventory = playerData["inventory"]
