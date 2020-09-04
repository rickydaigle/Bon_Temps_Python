#!/usr/bin/env python3

class Mob:

    MOB_LIST = [
        {"name":"Giant Nutria", "level":1, "maxHealth":15, "attack":6, "defense":3, "defenseChance":0.1, "exp":15, "bones":5, "attackVerb":"bite", "defenseVerb":"avoid"},
        {"name":"T'Frere", "level":8, "maxHealth":260, "attack":19, "defense":11, "defenseChance":0.25, "exp":3500, "bones":150, "attackVerb":"haunt", "defenseVerb":"absorb"},
        {"name":"Rougarou", "level":3, "maxHealth":50, "attack":9, "defense":6, "defenseChance":0.1, "exp":60, "bones":15, "attackVerb":"slash", "defenseVerb":"block"},
        {"name":"Tataille", "level":2, "maxHealth":25, "attack":7, "defense":5, "defenseChance":0.1, "exp":30, "bones":10, "attackVerb":"haunt", "defenseVerb":"absorb"},
        {"name":"Man-eating Gator", "level":4, "maxHealth":60, "attack":10, "defense":6, "defenseChance":0.1, "exp":120, "bones":65, "attackVerb":"haunt", "defenseVerb":"absorb"},
        {"name":"Snapping Turtle", "level":2, "maxHealth":20, "attack":8, "defense":5, "defenseChance":0.2, "exp":30, "bones":10, "attackVerb":"bite", "defenseVerb":"hide from"}
        ]
  
    def __init__(self, listNumber, mobID):
        self.name = Mob.MOB_LIST[listNumber]["name"]
        self.mobId = mobID
        self.level = Mob.MOB_LIST[listNumber]["level"]
        self.maxHealth = Mob.MOB_LIST[listNumber]["maxHealth"]
        self.health = Mob.MOB_LIST[listNumber]["maxHealth"]
        self.attack = Mob.MOB_LIST[listNumber]["attack"]
        self.attackVerb = Mob.MOB_LIST[listNumber]["attackVerb"]
        self.defense = Mob.MOB_LIST[listNumber]["defense"]
        self.defenseVerb = Mob.MOB_LIST[listNumber]["defenseVerb"]
        self.defenseChance = Mob.MOB_LIST[listNumber]["defenseChance"]
        self.exp = Mob.MOB_LIST[listNumber]["exp"]
        self.bones = Mob.MOB_LIST[listNumber]["bones"]
        self.isAlive = True
        self.lowHealth = False

    def print_name(self):
        return str(self.name)

    def get_attack_verb(self):
        return str(self.attackVerb)

    def get_defense_verb(self):
        return str(self.defenseVerb)

    def get_level(self):
        return self.level

    def get_id(self):
        return self.mobId

    def get_attack(self):
        return self.attack

    def get_exp(self):
        return self.exp

    def get_bones(self):
        return self.bones

    def get_defense(self):
        return self.defense

    def get_defense_chance(self):
        return self.defenseChance

    def lose_health(self, health):
        self.health -= int(round(health))
        if self.health <= 0:
            self.mob_dead()
        elif self.health <= (self.maxHealth * 0.2):
            self.lowHealth = True

    def mob_alive(self):
        if self.isAlive:
            return True
        else:
            return False

    def mob_dead(self):
        self.isAlive = False

    def get_health(self):
        healthStatus = str(self.health) + "/" + str(self.maxHealth)
        return healthStatus
