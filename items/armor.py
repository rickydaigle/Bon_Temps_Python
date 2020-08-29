#!/usr/bin/env python3

class Armor:
       
    ARMOR = {
        "Festival T-Shirt":{"defense":2, "value":6, "itemClass":"newb", "desc":"+02 Defense"},
        "Offshore Overalls":{"defense":5, "value":10, "itemClass":"hunter", "desc":"+05 Defense - Hunter Classes Only"},
        "Cotton Affliction Shirt":{"defense":3, "value":8, "itemClass":"voodoo", "desc":"+03 Defense - Voodoo Classes Only"},
        "Denim Downtown Alive Jacket":{"defense":8, "value":15, "itemClass":"hunter", "desc":"+08 Defense - Hunter Classes Only"},
        "Hunting Camo":{"defense":15, "value":25, "itemClass":"hunter", "desc":"+15 Defense - Hunter Classes Only"},
        "Gold Silk Saints Robe":{"defense":10, "value":16, "itemClass":"voodoo", "desc":"+10 Defense - Voodoo Classes Only"},
        "Green Silk IceGators Robe":{"defense":10, "value":16, "itemClass":"voodoo", "desc":"+10 Defense - Voodoo Classes Only"},
        "Red Silk Ragin' Cajuns Robe":{"defense":10, "value":16, "itemClass":"voodoo", "desc":"+10 Defense - Voodoo Classes Only"},
        "Purple LSU Home Jersey":{"defense":30, "value":55, "itemClass":"hero", "desc":"+30 Defense - Hero Classes Only"},
        "White LSU Away Jersey":{"defense":30, "value":55, "itemClass":"hero", "desc":"+30 Defense - Hero Classes Only"},
        "Armani Suit from Brother's on the Boulevard":{"defense":50, "value":175, "itemClass":"master", "desc":"+50 Defense - Master Classes Only"},
        "Fire-retardent Jumpsuit covered in Tony Chachere's":{"defense":25, "value":150, "itemClass":"mambo", "desc":"+25 Defense - Mambo Classes Only"}
        }

    def get_real_name(armorName):
        for each in Armor.ARMOR:
            if each.lower() == armorName.lower():
                return each
        return False

    def get_stats(armorName):
        if armorName in Armor.ARMOR:
            defense = Armor.ARMOR[armorName]["defense"]
            return defense
        else:
            return False

    def check_class(armorName, playerClass):
        if Armor.ARMOR[armorName]["itemClass"] == playerClass:
            return True
        else:
            return False

    def get_all_class(itemClass):
        armorNames = []
        for each in Armor.ARMOR:
            if Armor.ARMOR[each]["itemClass"] == itemClass:
                armorNames.append(each)
        return armorNames

    def get_shop_data(armorNames):
        shopData = []
        if isinstance(armorNames, list):
            for each in armorNames:
                armorIndex = []
                armorIndex.append(each)
                armorIndex.append(Armor.ARMOR[each]["value"])
                armorIndex.append(Armor.ARMOR[each]["desc"])
                shopData.append(armorIndex)
        else:
            shopData.append(armorNames)
            shopData.append(Armor.ARMOR[armorNames]["value"])
            shopData.append(Armor.ARMOR[armorNames]["desc"])
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
        maxNameLen, maxValueLen = Armor.get_max_lengths(shopData)
        print("#".ljust(itemJust) + "Name".ljust(maxNameLen + nameJust) + "Cost".ljust(maxValueLen + valueJust) + "Description")
        for i, each in enumerate(shopData):
            print(str(i+1).ljust(itemJust) + str(each[0]).ljust(maxNameLen + nameJust) + str(each[1]).ljust(maxValueLen + valueJust) + str(each[2]))
    
    print("Current armor list:")
    for each in Armor.ARMOR:
        print()
        print(str(each))
        defense = Armor.get_stats(each)
        print("   Defense: {}".format(defense))
        shopData = Armor.get_shop_data(each)
        print("   Name: {} | Value: {} | Description: {}".format(shopData[0], shopData[1], shopData[2]))
        print("   Armor Class: {}".format(Armor.ARMOR[each]["itemClass"]))
        print("   Is this for newbs? {}".format(Armor.check_class(each, "newb")))
        print("   Is this for hunters? {}".format(Armor.check_class(each, "hunter")))
        print("   Is this for heroes? {}".format(Armor.check_class(each, "hero")))
        print("   Is this for voodoos? {}".format(Armor.check_class(each, "voodoo")))
        print("   Is this for mambos? {}".format(Armor.check_class(each, "mambo")))
        print("   Is this for masters? {}".format(Armor.check_class(each, "master")))
    newbs = Armor.get_all_class("newb")
    hunters = Armor.get_all_class("hunter")
    heroes = Armor.get_all_class("hero")
    voodoos = Armor.get_all_class("voodoo")
    mambos = Armor.get_all_class("mambo")
    masters = Armor.get_all_class("master")
    itemJust = 4
    nameJust = 2
    valueJust = 4
    print("\nNewb Armor:")
    for each in newbs:
        print(each)
    shopData = Armor.get_shop_data(newbs)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nHunter Armor:")
    for each in hunters:
        print(each)
    shopData = Armor.get_shop_data(hunters)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nHero Armor:")
    for each in heroes:
        print(each)
    shopData = Armor.get_shop_data(heroes)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nVoodoo Armor:")
    for each in voodoos:
        print(each)
    shopData = Armor.get_shop_data(voodoos)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nMambo Armor:")
    for each in mambos:
        print(each)
    shopData = Armor.get_shop_data(mambos)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print("\nMaster Armor:")
    for each in masters:
        print(each)
    shopData = Armor.get_shop_data(masters)
    print_shop_format(shopData, itemJust, nameJust, valueJust)
    print()
    input("Press Enter to exit test...")
             
if __name__ == "__main__":
    unit_test()
