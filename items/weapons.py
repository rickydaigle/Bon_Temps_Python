#!/usr/bin/env python3

class Weapons:
       
    WEAPONS = {
        "LPCC Shiv":{"attack":4, "attackAction":"stab", "defense":3, "defenseAction":"deflect", "defenseChance":0.1, "value":16, "itemClass":"newb", "desc":"+04 Attack, +03 Defense, 10% block chance"},
        "Lil' Pocket Knife":{"attack":5, "attackAction":"slash", "defense":2, "defenseAction":"parry", "defenseChance":0.1, "value":16, "itemClass":"hunter", "desc":"+05 Attack, +02 Defense, 10% block chance - Hunters Only"},
        "French Dagger":{"attack":5, "attackAction":"slash", "defense":3, "defenseAction":"parry", "defenseChance":0.1, "value":21, "itemClass":"hunter", "desc":"+05 Attack, +03 Defense, 10% block chance - Hunters Only"},
        "Rambo Knife":{"attack":8, "attackAction":"slash", "defense":7, "defenseAction":"parry", "defenseChance":0.1, "value":36, "itemClass":"hero", "desc":"+08 Attack, +07 Defense, 10% block chance - Heroes Only"},
        "Bayonet":{"attack":10, "attackAction":"slash", "defense":5, "defenseAction":"parry", "defenseChance":0.15, "value":36, "itemClass":"hero", "desc":"+10 Attack, +05 Defense, 15% block chance - Heroes Only"},
        "Wand":{"attack":6, "attackAction":"blast", "defense":0, "defenseAction":"dissipate", "defenseChance":0.05, "value":16, "itemClass":"voodoo", "desc":"+06 Attack, +00 Defense, 05% block chance - Voodoos Only"},
        "Grisgris Wand":{"attack":10, "attackAction":"blast", "defense":3, "defenseAction":"dissipate", "defenseChance":0.1, "value":40, "itemClass":"mambo", "desc":"+10 Attack, +03 Defense, 10% block chance - Mambos Only"},
        "Tataille Wand":{"attack":12, "attackAction":"burn", "defense":2, "defenseAction":"dissipate", "defenseChance":0.1, "value":40, "itemClass":"mambo", "desc":"+12 Attack, +02 Defense, 10% block chance - Mambos Only"},
        "Rougarou Wand":{"attack":14, "attackAction":"drain", "defense":1, "defenseAction":"dissipate", "defenseChance":0.1, "value":40, "itemClass":"mambo", "desc":"+14 Attack, +01 Defense, 10% block chance - Mambos Only"},
        "Glowing Bayonet":{"attack":25, "attackAction":"slice", "defense":15, "defenseAction":"parry", "defenseChance":0.2, "value":120, "itemClass":"master", "desc":"+25 Attack, +15 Defense, 20% block chance - Swamp Masters Only"}
        }

    def get_real_name(weaponName):
        for each in Weapons.WEAPONS:
            if each.lower() == weaponName.lower():
                return each
        return False

    def get_stats(weaponName):
        if weaponName in Weapons.WEAPONS:
            attack = Weapons.WEAPONS[weaponName]["attack"]
            defense = Weapons.WEAPONS[weaponName]["defense"]
            return attack, defense
        else:
            return False, False

    def get_actions(weaponName):
        if weaponName in Weapons.WEAPONS:
            attackAction = Weapons.WEAPONS[weaponName]["attackAction"]
            defenseAction = Weapons.WEAPONS[weaponName]["defenseAction"]
            return attackAction, defenseAction
        else:
            return False, False

    def check_class(weaponName, playerClass):
        if Weapons.WEAPONS[weaponName]["itemClass"] == playerClass:
            return True
        else:
            return False

    def get_all_class(itemClass):
        weaponNames = []
        for each in Weapons.WEAPONS:
            if Weapons.WEAPONS[each]["itemClass"] == itemClass:
                weaponNames.append(each)
        return weaponNames

    def get_shop_data(weaponNames):
        shopData = []
        if isinstance(weaponNames, list):
            for each in weaponNames:
                weaponIndex = []
                weaponIndex.append(each)
                weaponIndex.append(Weapons.WEAPONS[each]["value"])
                weaponIndex.append(Weapons.WEAPONS[each]["desc"])
                shopData.append(weaponIndex)
        else:
            shopData.append(weaponNames)
            shopData.append(Weapons.WEAPONS[weaponNames]["value"])
            shopData.append(Weapons.WEAPONS[weaponNames]["desc"])
        return shopData

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
            if len(each[0]) > maxNameLen:
                maxNameLen = len(each[0])
            if len(str(each[1])) > maxValueLen:
                maxValueLen = len(str(each[1]))
        return maxNameLen, maxValueLen

def unit_test():

    def print_shop_format(shopData, itemJust, nameJust, valueJust):
        maxNameLen, maxValueLen = Weapons.get_max_lengths(shopData)
        print("#".ljust(itemJust) + "Name".ljust(maxNameLen + nameJust) + "Cost".ljust(maxValueLen + valueJust) + "Description")
        for i, each in enumerate(shopData):
            print(str(i+1).ljust(itemJust) + str(each[0]).ljust(maxNameLen + nameJust) + str(each[1]).ljust(maxValueLen + valueJust) + str(each[2]))
        
    print("Current weapon list:")
    for each in Weapons.WEAPONS:
        print()
        print(str(each))
        attack, defense = Weapons.get_stats(each)
        attackAction, defenseAction = Weapons.get_actions(each)
        print("   Attack: {} for {} | Defense: {} for {}".format(attackAction, attack, defenseAction, defense))
        shopData = Weapons.get_shop_data(each)
        print("   Name: {} | Value: {} | Description: {}".format(shopData[0], shopData[1], shopData[2]))
        print("   Weapon Class: {}".format(Weapons.WEAPONS[each]["itemClass"]))
        print("   Is this for Newbs? {}".format(Weapons.check_class(each, "newb")))
        print("   Is this for Hunters? {}".format(Weapons.check_class(each, "hunter")))
        print("   Is this for Heroes? {}".format(Weapons.check_class(each, "hero")))
        print("   Is this for Voodoos? {}".format(Weapons.check_class(each, "voodoo")))
        print("   Is this for Mambos? {}".format(Weapons.check_class(each, "mambo")))
        print("   Is this for Swamp Masters? {}".format(Weapons.check_class(each, "master")))
    newbs = Weapons.get_all_class("newb")
    hunters = Weapons.get_all_class("hunter")
    heroes = Weapons.get_all_class("hero")
    voodoos = Weapons.get_all_class("voodoo")
    mambos = Weapons.get_all_class("mambo")
    masters = Weapons.get_all_class("master")
    itemJust = 4
    nameJust = 2
    valueJust = 4
    print("\nNewb Weapons:")
    for each in newbs:
        print(each)
    shopData = Weapons.get_shop_data(newbs)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nHunter Weapons:")
    for each in hunters:
        print(each)
    shopData = Weapons.get_shop_data(hunters)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nHero Weapons:")
    for each in heroes:
        print(each)
    shopData = Weapons.get_shop_data(heroes)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nVoodoo Weapons:")
    for each in voodoos:
        print(each)
    shopData = Weapons.get_shop_data(voodoos)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nMambo Weapons:")
    for each in mambos:
        print(each)
    shopData = Weapons.get_shop_data(mambos)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nSwamp Master Weapons:")
    for each in masters:
        print(each)
    shopData = Weapons.get_shop_data(masters)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    input("Press Enter to exit test...")
             
if __name__ == "__main__":
    unit_test()
